import React, { useState } from "react";
import { FaEye, FaEyeSlash } from 'react-icons/fa';
import "./LoginPage.css";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    if (!email || !password) {
      setError("Please enter Email and Password!");
      return;
    }

    try {
      const response = await fetch("http://localhost:8989/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          user_email: email,
          password: password,
        }),
      });
      if (!response.ok) {
        throw new Error("Login failed");
      }

      const data = await response.json();
      console.log("Login Successful: ", data);

      setError("");
      alert("Login Successful!!");
    } catch (err) {
      console.log("Login Error: ", err);
      setError("Invalid credentials or server error.");
    }
  };

  return (
    <div className="login-container">
        <h1 className="app-title">ToDoFlix</h1>

      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        {error && <p className="error">{error}</p>}

        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            value={email}
            placeholder="Enter email"
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <div className="form-group password-group">
          <label>Password:</label>
          <div className="password-input">
            <input
              type={showPassword ? 'text' : 'password'}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password"
            />
            <span
              className="password-toggle-icon"
              onClick={() => setShowPassword(!showPassword)}
              role="button"
              aria-label={showPassword ? 'Hide password' : 'Show password'}
              tabIndex={0}
              onKeyDown={(e) => { if (e.key === 'Enter') setShowPassword(!showPassword)}}
            >
              {showPassword ? <FaEyeSlash /> : <FaEye />}
            </span>
          </div>
        </div>
        <button type="submit" className="login-btn">
          Login
        </button>
        <p style={{ textAlign: "center", marginTop: "15px" }}>
          Don’t have an account?{" "}
          <a href="/signup" style={{ color: "#E50914" }}>
            Sign up
          </a>
        </p>
      </form>
    </div>
  );
};

export default LoginPage;
