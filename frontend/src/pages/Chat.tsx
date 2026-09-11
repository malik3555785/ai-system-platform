import React, { useState } from 'react';
import axios from 'axios';
import './Pages.css';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
}

function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [model, setModel] = useState('gpt-4');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage: Message = {
      role: 'user',
      content: input,
      timestamp: new Date().toISOString()
    };
    
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);
    setError('');

    try {
      const response = await axios.post('http://localhost:8000/api/v1/chat/message', {
        content: input,
        model: model,
        temperature: 0.7
      });

      const assistantMessage: Message = {
        role: 'assistant',
        content: response.data.message,
        timestamp: response.data.timestamp
      };
      
      setMessages(prev => [...prev, assistantMessage]);
    } catch (err) {
      setError('Failed to send message. Please try again.');
      console.error('Chat error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div className="chat-container">
        <div className="chat-header">
          <h1>Chat with AI</h1>
          <div className="model-info">Using: {model}</div>
        </div>
        
        <div className="chat-messages">
          {messages.length === 0 ? (
            <div className="empty-state">
              <p>No messages yet. Start a conversation!</p>
            </div>
          ) : (
            messages.map((msg, idx) => (
              <div key={idx} className={`message ${msg.role}`}>
                <div className="message-content">
                  <p>{msg.content}</p>
                </div>
                <small>{new Date(msg.timestamp).toLocaleTimeString()}</small>
              </div>
            ))
          )}
          {loading && (
            <div className="message assistant">
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span><span></span><span></span>
                </div>
              </div>
            </div>
          )}
        </div>

        {error && <div className="alert alert-error">{error}</div>}

        <form onSubmit={sendMessage} className="chat-form">
          <select 
            value={model} 
            onChange={(e) => setModel(e.target.value)}
            className="model-select"
          >
            <option value="gpt-4">GPT-4</option>
            <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
            <option value="claude-3">Claude 3</option>
            <option value="claude-2">Claude 2</option>
          </select>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            disabled={loading}
            className="message-input"
          />
          <button type="submit" disabled={loading} className="send-btn">
            {loading ? '⏳' : '✉️'} Send
          </button>
        </form>
      </div>
    </div>
  );
}

export default Chat;
