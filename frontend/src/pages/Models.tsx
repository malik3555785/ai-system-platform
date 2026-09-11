import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Pages.css';

interface Model {
  name: string;
  provider: string;
  version: string;
  description: string;
  enabled: boolean;
}

function Models() {
  const [models, setModels] = useState<Model[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [initialized, setInitialized] = useState<Set<string>>(new Set());

  useEffect(() => {
    fetchModels();
  }, []);

  const fetchModels = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/v1/models/list');
      setModels(response.data.models);
      setLoading(false);
    } catch (err) {
      setError('Failed to fetch models');
      setLoading(false);
      console.error(err);
    }
  };

  const initializeModel = async (modelName: string) => {
    try {
      await axios.post(`http://localhost:8000/api/v1/models/initialize?model_name=${modelName}`);
      setInitialized(prev => new Set(prev).add(modelName));
      alert(`✓ Model ${modelName} initialized successfully!`);
    } catch (err) {
      alert(`✗ Failed to initialize model: ${err}`);
    }
  };

  return (
    <div className="page-container">
      <h1>Available AI Models</h1>
      {loading && <p className="loading">Loading models...</p>}
      {error && <p className="error">{error}</p>}
      
      <div className="models-grid">
        {models.map((model) => (
          <div key={model.name} className="model-card">
            <div className="card-header">
              <h3>{model.name}</h3>
              <span className={`provider-badge ${model.provider.toLowerCase()}`}>
                {model.provider}
              </span>
            </div>
            <div className="card-body">
              <p className="description">{model.description}</p>
              <div className="model-details">
                <span className="detail"><strong>Version:</strong> {model.version}</span>
                <span className="detail"><strong>Status:</strong> {model.enabled ? '✓ Available' : '✗ Unavailable'}</span>
              </div>
            </div>
            <button
              onClick={() => initializeModel(model.name)}
              disabled={!model.enabled || initialized.has(model.name)}
              className={`init-btn ${initialized.has(model.name) ? 'initialized' : ''}`}
            >
              {initialized.has(model.name) ? '✓ Initialized' : 'Initialize'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Models;
