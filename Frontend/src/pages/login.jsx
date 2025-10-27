import React, { useState } from "react";
import API from "../api";
import { saveToken } from "../auth";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const nav = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // FastAPI's token endpoint expects form data username/password
      const formData = new URLSearchParams();
      formData.append("username", email);
      formData.append("password", password);
      const res = await API.post("/api/users/login", formData.toString(), {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      });
      saveToken(res.data.access_token);
      nav("/");
    } catch (err) {
      alert("Login failed: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div style={{ maxWidth: 420 }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div><input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} /></div>
        <div><input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} /></div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
