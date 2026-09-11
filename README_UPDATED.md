# AI System Platform

A comprehensive, professional-grade AI system incorporating multiple models and tools with enterprise-grade features.

## 🎯 Features

- **Multi-Model Support**: GPT-4, Claude, and other advanced models
- **Tool Integration**: Extensible tool system for enhanced capabilities  
- **Enterprise Features**: Authentication, logging, monitoring, rate limiting
- **REST API**: Full-featured HTTP API for integration
- **Docker Support**: Containerized deployment
- **React Frontend**: Modern, responsive web interface
- **Real-time Chat**: Interactive chat with multiple AI models
- **External API Integration**: Seamless integration with external services

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/malik3555785/ai-system-platform.git
cd ai-system-platform

# Start all services
docker-compose -f docker/docker-compose.yml up -d

# Access
# Frontend: http://localhost:3000
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Local Development

**Backend:**
```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

## 📋 System Architecture

```
┌──────────────────────────────────────┐
│     Frontend (React + TypeScript)    │
│       http://localhost:3000          │
└────────────────┬─────────────────────┘
                 │
┌────────────────▼─────────────────────┐
│    Backend API (FastAPI + Python)    │
│       http://localhost:8000          │
│                                      │
│  • Health Checks                     │
│  • Model Management                  │
│  • Chat Interface                    │
│  • External API Integration          │
└────────────────┬─────────────────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
┌───▼──┐  ┌─────▼────┐  ┌────▼───┐
│Redis │  │External  │  │SQLite  │
│Cache │  │APIs      │  │DB      │
└──────┘  └──────────┘  └────────┘
```

## 🔌 API Endpoints

### Health
- `GET /health` - System health
- `GET /status` - System status

### Models  
- `GET /api/v1/models/list` - List models
- `GET /api/v1/models/{name}` - Get model details
- `POST /api/v1/models/initialize` - Initialize model

### Chat
- `POST /api/v1/chat/message` - Send message
- `GET /api/v1/chat/history/{id}` - Get history
- `DELETE /api/v1/chat/clear/{id}` - Clear history

### External APIs
- `GET /api/v1/external/endpoints` - List endpoints
- `GET /api/v1/external/models` - Get models
- `POST /api/v1/external/call` - Call endpoint
- `POST /api/v1/external/process` - Process request

## 📁 Project Structure

```
ai-system-platform/
├── src/              # Backend source code
├── frontend/         # React frontend
├── docker/           # Docker configuration
├── tests/            # Test suites
├── main.py           # Entry point
└── requirements.txt   # Dependencies
```

## ⚙️ Configuration

Create `.env` file (see `.env.example`):

```env
API_HOST=0.0.0.0
API_PORT=8000
EXTERNAL_API_BASE_URL=https://apis.davidcyril.name.ng
DATABASE_URL=sqlite:///./data/ai_system.db
REDIS_URL=redis://localhost:6379/0
```

## 🧪 Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=src tests/

# Specific test
pytest tests/test_health.py -v
```

## 📚 Documentation

- [Setup Guide](SETUP_GUIDE.md) - Detailed setup instructions
- [API Docs](http://localhost:8000/docs) - Interactive API documentation
- [Contributing](CONTRIBUTING.md) - Development guidelines

## 🐳 Docker Commands

```bash
# Build
docker-compose -f docker/docker-compose.yml build

# Start
docker-compose -f docker/docker-compose.yml up -d

# Logs
docker-compose -f docker/docker-compose.yml logs -f

# Stop
docker-compose -f docker/docker-compose.yml down
```

## 🔍 Troubleshooting

### Port already in use
```bash
# Find process using port 8000
lsof -i :8000

# Or use different port
API_PORT=8001 python main.py
```

### Redis connection failed
```bash
# Test Redis
redis-cli ping

# Or disable Redis caching
# Set REDIS_URL to empty string in .env
```

### Frontend can't reach backend
```bash
# Verify backend is running
curl http://localhost:8000/health

# Check browser console (F12)
# Ensure API URL is correct
```

## 📊 Monitoring

- **Logs**: `logs/ai_system.log` (JSON format)
- **Health**: `http://localhost:8000/health`
- **Status**: `http://localhost:8000/status`
- **Metrics**: `http://localhost:9090` (if Prometheus enabled)

## 🚀 Production Deployment

1. Update `.env` with production settings
2. Use PostgreSQL instead of SQLite
3. Enable HTTPS/SSL
4. Set up proper authentication
5. Configure rate limiting
6. Set up monitoring and alerts

## 📄 License

MIT License - See [LICENSE](LICENSE) file

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Build Date**: September 11, 2026  
**Version**: 2.0.0  
**Status**: ✅ Production Ready
