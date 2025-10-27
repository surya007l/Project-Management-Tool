import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { logout } from "../auth";

export default function Navbar() {
  const navigate = useNavigate();
  const handleLogout = () => {
    logout();
    navigate("/login");
  };
  return (
    <nav style={{ padding: 10, background: "#eee" }}>
      <Link style={{ marginRight: 10 }} to="/">Dashboard</Link>
      <Link style={{ marginRight: 10 }} to="/projects">Projects</Link>
      <Link style={{ marginRight: 10 }} to="/tasks">Tasks</Link>
      <Link style={{ marginLeft: 20 }} to="/login">Login</Link>
      <button style={{ marginLeft: 10 }} onClick={handleLogout}>Logout</button>
    </nav>
  );
}
