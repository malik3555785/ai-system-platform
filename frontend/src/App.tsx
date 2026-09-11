import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import Chat from './pages/Chat';
import Models from './pages/Models';
import ExternalAPIs from './pages/ExternalAPIs';
import './App.css';

function App() {
  const [isConnected, setIsConnected] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    checkBackendConnection();
  }, []);

  const checkBackendConnection = async () => {
    try {
      const response = await fetch('http://localhost:8000/health');
      if (response.ok) {
        setIsConnected(true);
        console.log('Connected to AI System Backend');
      }
    } catch (error) {
      console.warn('Backend not connected:', error);
      setIsConnected(false);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Router>
      <div className="App">
        <Navigation isConnected={isConnected} />
        <main className="main-content">
          {isLoading ? (
            <div className="loading-container">
              <div className="spinner"></div>
              <p>Connecting to AI System...</p>
            </div>
          ) : (
            <Routes>
              <Route path="/" element={<Home isConnected={isConnected} />} />
              <Route path="/chat" element={<Chat />} />
              <Route path="/models" element={<Models />} />
              <Route path="/external-apis" element={<ExternalAPIs />} />
            </Routes>
          )}
        </main>
      </div>
    </Router>
  );
}

export default App;
