import React from 'react';
import './Pages.css';

interface HomeProps {
  isConnected: boolean;
}

function Home({ isConnected }: HomeProps) {
  return (
    <div className="page-container">
      <div className="hero">
        <h1>Welcome to AI System Platform</h1>
        <p className="subtitle">Comprehensive professional-grade AI system with multi-model support</p>
        
        {!isConnected && (
          <div className="alert alert-warning">
            ⚠️ Backend connection unavailable. Some features may not work properly.
          </div>
        )}
        
        <div className="features">
          <div className="feature-card">
            <div className="feature-icon">🧠</div>
            <h3>Multi-Model Support</h3>
            <p>Access GPT-4, Claude, and other advanced AI models</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🔧</div>
            <h3>Tool Integration</h3>
            <p>Extensible tool system for enhanced capabilities</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🚀</div>
            <h3>Enterprise Ready</h3>
            <p>Authentication, logging, monitoring, and rate limiting</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🌐</div>
            <h3>External APIs</h3>
            <p>Seamless integration with external AI services</p>
          </div>
        </div>

        <div className="cta-section">
          <h2>Get Started</h2>
          <div className="cta-buttons">
            <a href="/chat" className="btn btn-primary">Start Chatting</a>
            <a href="/models" className="btn btn-secondary">Explore Models</a>
            <a href="/external-apis" className="btn btn-secondary">View APIs</a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
