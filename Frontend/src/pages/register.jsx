import React, { useState } from "react";
import API from "../api";

function Register() {
  const [name,setName] = useState("");
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");
  const [role,setRole] = useState("developer");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await API.post("/api/users/register", { name, email, password, role });
      alert("Registered. Please login.");
    } catch (err) {
      alert("Error: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <div><input placeholder="Name" value={name} onChange={e => setName(e.target.value)} /></div>
        <div><input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} /></div>
        <div><input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} /></div>
        <div>
          <select value={role} onChange={e => setRole(e.target.value)}>
            <option value="developer">Developer</option>
            <option value="manager">Manager</option>
            <option value="admin">Admin</option>
          </select>
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;
