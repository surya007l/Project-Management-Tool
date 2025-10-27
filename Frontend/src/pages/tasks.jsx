import React, {useEffect, useState} from "react";
import API from "../api";
import { authHeader } from "../auth";

export default function Tasks() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [projectId, setProjectId] = useState("");
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    const fetch = async () => {
      const p = await API.get("/api/projects", { headers: authHeader() });
      setProjects(p.data);
      const t = await API.get("/api/tasks", { headers: authHeader() });
      setTasks(t.data);
    };
    fetch();
  }, []);

  const create = async (e) => {
    e.preventDefault();
    try {
      await API.post("/api/tasks", { title, project_id: parseInt(projectId) }, { headers: authHeader() });
      setTitle("");
      const t = await API.get("/api/tasks", { headers: authHeader() });
      setTasks(t.data);
    } catch (err) {
      alert("Error: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div>
      <h2>Tasks</h2>
      <form onSubmit={create}>
        <input placeholder="Title" value={title} onChange={e=>setTitle(e.target.value)} />
        <select value={projectId} onChange={e => setProjectId(e.target.value)}>
          <option value="">Select project</option>
          {projects.map(p => <option key={p.id} value={p.id}>{p.name}</option>)}
        </select>
        <button>Create</button>
      </form>
      <ul>
        {tasks.map(t => <li key={t.id}>{t.title} — {t.status}</li>)}
      </ul>
    </div>
  );
}
