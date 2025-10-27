import React, { useEffect, useState } from "react";
import API from "../api";
import { authHeader } from "../auth";

export default function Dashboard() {
  const [projects, setProjects] = useState([]);
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const fetch = async () => {
      try {
        const p = await API.get("/api/projects", { headers: authHeader() });
        setProjects(p.data);
        const t = await API.get("/api/tasks", { headers: authHeader() });
        setTasks(t.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetch();
  }, []);

  const overdue = tasks.filter(t => t.deadline && new Date(t.deadline) < new Date()).length;
  const todo = tasks.filter(t => t.status === "To Do").length;
  const inprogress = tasks.filter(t => t.status === "In Progress").length;
  const done = tasks.filter(t => t.status === "Done").length;

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Projects: {projects.length}</p>
      <p>Tasks total: {tasks.length} — Overdue: {overdue}</p>
      <ul>
        <li>To Do: {todo}</li>
        <li>In Progress: {inprogress}</li>
        <li>Done: {done}</li>
      </ul>
    </div>
  );
}
