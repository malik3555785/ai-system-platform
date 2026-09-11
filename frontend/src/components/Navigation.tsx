import React from 'react';
import { Link } from 'react-router-dom';
import './Navigation.css';

interface NavigationProps {
  isConnected: boolean;
}

function Navigation({ isConnected }: NavigationProps) {
  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          <span className="logo-icon">����</span>
          AI System Platform
        </Link>
        <ul className="nav-menu">
          <li className="nav-item">
            <Link to="/" className="nav-link">Home</Link>
          </li>
          <li className="nav-item">
            <Link to="/chat" className="nav-link">Chat</Link>
          </li>
          <li className="nav-item">
            <Link to="/models" className="nav-link">Models</Link>
          </li>
          <li className="nav-item">
            <Link to="/external-apis" className="nav-link">External APIs</Link>
          </li>
          <li className="nav-item status-indicator">
            <span className={`status ${isConnected ? 'connected' : 'disconnected'}`}>
              {isConnected ? '● Connected' : '● Disconnected'}
            </span>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navigation;
