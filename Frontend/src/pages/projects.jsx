import React, {useEffect, useState} from "react";
import API from "../api";
import { authHeader } from "../auth";

export default function Projects() {
  const [projects, setProjects] = useState([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const fetch = async () => {
    const res = await API.get("/api/projects", { headers: authHeader() });
    setProjects(res.data);
  };

  useEffect(() => { fetch(); }, []);

  const create = async e => {
    e.preventDefault();
    try {
      await API.post("/api/projects", { name, description }, { headers: authHeader() });
      setName(""); setDescription("");
      fetch();
    } catch (err) {
      alert("Error: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div>
      <h2>Projects</h2>
      <form onSubmit={create}>
        <input placeholder="Name" value={name} onChange={e=>setName(e.target.value)} />
        <input placeholder="Description" value={description} onChange={e=>setDescription(e.target.value)} />
        <button>Create</button>
      </form>
      <ul>
        {projects.map(p => <li key={p.id}>{p.name} - {p.status}</li>)}
      </ul>
    </div>
  );
}
