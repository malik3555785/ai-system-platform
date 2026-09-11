import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Pages.css';

function ExternalAPIs() {
  const [endpoints, setEndpoints] = useState<any[]>([]);
  const [models, setModels] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [activeTab, setActiveTab] = useState<'endpoints' | 'models'>('endpoints');

  useEffect(() => {
    fetchExternalData();
  }, []);

  const fetchExternalData = async () => {
    try {
      const [endpointsRes, modelsRes] = await Promise.all([
        axios.get('http://localhost:8000/api/v1/external/endpoints').catch(() => ({ data: { endpoints: [] } })),
        axios.get('http://localhost:8000/api/v1/external/models').catch(() => ({ data: { models: [] } }))
      ]);
      
      setEndpoints(endpointsRes.data.endpoints || []);
      setModels(modelsRes.data.models || []);
      setLoading(false);
    } catch (err) {
      setError('Failed to fetch external APIs');
      setLoading(false);
      console.error(err);
    }
  };

  return (
    <div className="page-container">
      <h1>External API Integration</h1>
      <p className="subtitle">Integrate with https://apis.davidcyril.name.ng</p>
      
      {loading && <p className="loading">Loading external APIs...</p>}
      {error && <p className="error">{error}</p>}
      
      <div className="tabs">
        <button 
          className={`tab ${activeTab === 'endpoints' ? 'active' : ''}`}
          onClick={() => setActiveTab('endpoints')}
        >
          Endpoints
        </button>
        <button 
          className={`tab ${activeTab === 'models' ? 'active' : ''}`}
          onClick={() => setActiveTab('models')}
        >
          Models
        </button>
      </div>

      {activeTab === 'endpoints' && (
        <div className="section">
          <div className="endpoints-list">
            {endpoints && endpoints.length > 0 ? (
              endpoints.map((endpoint, idx) => (
                <div key={idx} className="endpoint-item">
                  <div className="endpoint-icon">📡</div>
                  <div className="endpoint-info">
                    <p className="endpoint-name">{typeof endpoint === 'string' ? endpoint : endpoint.name || endpoint.path}</p>
                    <p className="endpoint-desc">{endpoint.description || 'External API Endpoint'}</p>
                  </div>
                </div>
              ))
            ) : (
              <div className="empty-state">No endpoints available</div>
            )}
          </div>
        </div>
      )}

      {activeTab === 'models' && (
        <div className="section">
          <div className="models-list">
            {models && models.length > 0 ? (
              models.map((model, idx) => (
                <div key={idx} className="model-item">
                  <div className="model-icon">🤖</div>
                  <div className="model-info">
                    <p className="model-name">{model.name || model}</p>
                    <p className="model-desc">{model.description || 'AI Model'}</p>
                  </div>
                </div>
              ))
            ) : (
              <div className="empty-state">No models available</div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default ExternalAPIs;
