import React, { useState } from 'react';
import './Register.css';

const Register = ({ onClose }) => {
  const [userName, setUserName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const register = async (e) => {
    e.preventDefault();
    // Logic xử lý đăng ký tài khoản
  };

  return (
    <div className="register-container">
      <h2>SignUp</h2>
      <form onSubmit={register}>
        <div className="input-field">
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            required
          />
        </div>
        <div className="input-field">
          <input
            type="text"
            name="first_name"
            placeholder="First Name"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </div>
        <div className="input-field">
          <input
            type="text"
            name="last_name"
            placeholder="Last Name"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </div>
        <div className="input-field">
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="input-field">
          {/* Đã sửa placeholder thành 'Password' thay vì 'name' */}
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div className="submit-field">
          <button type="submit" className="register-button">Register</button>
        </div>
      </form>
    </div>
  );
};

export default Register;