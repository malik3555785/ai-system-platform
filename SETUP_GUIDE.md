# AI System Platform - Complete Documentation

## 📋 Overview

The AI System Platform is a **comprehensive, professional-grade AI system** that integrates multiple AI models and external APIs with a full-stack web application.

### ✨ Key Features

- **Multi-Model Support**: GPT-4, GPT-3.5 Turbo, Claude 3, Claude 2
- **External API Integration**: https://apis.davidcyril.name.ng
- **Real-Time Chat**: Interactive chat interface with multiple models
- **Enterprise Features**: Authentication, logging, monitoring, rate limiting
- **Fully Containerized**: Docker & Docker Compose support
- **Production Ready**: Comprehensive error handling and testing

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────┐
│           Frontend (React 18 + TypeScript)      │
│        Running on http://localhost:3000         │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│         API Gateway (FastAPI + Uvicorn)        │
│        Running on http://localhost:8000        │
│                                                  │
│  ├─ /health, /status (Health Check)            │
│  ├─ /api/v1/models (Model Management)          │
│  ├─ /api/v1/chat (Chat Interface)              │
│  └─ /api/v1/external (External APIs)           │
└──────────────────┬──────────────────────────────┘
                   │
      ┌────────────┼────────────┐
      │            │            │
  ┌───▼──┐  ┌─────▼────┐  ┌────▼───┐
  │Redis │  │ External │  │Database│
  │Cache │  │   APIs   │  │SQLite  │
  └──────┘  └──────────┘  └────────┘
```

## 📁 Project Structure

```
ai-system-platform/
├── backend/
│   ├── src/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── health.py      # Health checks
│   │   │   │   ├── models.py      # Model management
│   │   │   │   ├── chat.py        # Chat endpoints
│   │   │   │   └── external_apis.py # External API calls
│   │   │   └── app.py             # FastAPI app factory
│   │   ├── config/
│   │   │   └── settings.py        # Configuration
│   │   └── core/
│   │       ├── logger.py          # Logging setup
│   │       ├── database.py        # Database connection
│   │       └── cache.py           # Redis cache
│   ├── tests/
│   │   ├── test_health.py
│   │   ├── test_models.py
│   │   ├── test_chat.py
│   │   └── test_external_apis.py
│   ├── main.py                    # Entry point
│   └── requirements.txt            # Dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── Navigation.tsx
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Chat.tsx
│   │   │   ├── Models.tsx
│   │   │   └── ExternalAPIs.tsx
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   └── styles/
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── Dockerfile
│   └── .gitignore
└── docker/
    ├── Dockerfile              # Backend Docker image
    ├── docker-compose.yml      # Multi-container setup
    ├── nginx.conf              # Nginx reverse proxy
    └── .dockerignore
```

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Clone repository
git clone https://github.com/malik3555785/ai-system-platform.git
cd ai-system-platform

# Build and start all services
docker-compose -f docker/docker-compose.yml up -d

# Access services
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Local Development

#### Backend Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Run backend server
python main.py
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

## 🔌 API Endpoints

### Health Check
```bash
GET /health
GET /status
```

### Models
```bash
GET /api/v1/models/list              # List all models
GET /api/v1/models/{model_name}      # Get model details
POST /api/v1/models/initialize       # Initialize model
```

### Chat
```bash
POST /api/v1/chat/message            # Send message
GET /api/v1/chat/history/{session_id} # Get chat history
DELETE /api/v1/chat/clear/{session_id} # Clear history
```

### External APIs
```bash
GET /api/v1/external/endpoints       # List endpoints
GET /api/v1/external/models          # Get models
POST /api/v1/external/call           # Call endpoint
POST /api/v1/external/process        # Process request
```

## 📦 Environment Configuration

Create `.env` file:

```env
# API
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=False

# External API
EXTERNAL_API_BASE_URL=https://apis.davidcyril.name.ng
EXTERNAL_API_TIMEOUT=30
EXTERNAL_API_RETRY_ATTEMPTS=3

# Database
DATABASE_URL=sqlite:///./data/ai_system.db

# Cache
REDIS_URL=redis://localhost:6379/0

# Security
AUTH_SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_here

# System
SYSTEM_NAME=AI-System-Platform
SYSTEM_VERSION=2.0.0
ENVIRONMENT=development
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_health.py -v
```

## 📊 Monitoring

### Logs
- Location: `logs/ai_system.log`
- Format: JSON (easy parsing)
- Automatic rotation

### Health Check
```bash
curl http://localhost:8000/health
```

### API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🐳 Docker Commands

```bash
# Build images
docker-compose -f docker/docker-compose.yml build

# Start services
docker-compose -f docker/docker-compose.yml up -d

# View logs
docker-compose -f docker/docker-compose.yml logs -f backend

# Stop services
docker-compose -f docker/docker-compose.yml down

# Remove volumes
docker-compose -f docker/docker-compose.yml down -v
```

## 🔍 Troubleshooting

### Backend won't start
```bash
# Check logs
docker-compose -f docker/docker-compose.yml logs backend

# Verify port is not in use
lsof -i :8000
```

### Frontend connection issues
```bash
# Verify backend is running
curl http://localhost:8000/health

# Check browser console for errors
# (F12 → Console tab)
```

### Redis connection issues
```bash
# Test Redis connection
redis-cli ping

# Check Redis status
redis-cli info server
```

## 📝 Features Checklist

- ✅ Multi-model AI support
- ✅ Real-time chat interface
- ✅ External API integration
- ✅ Health checks and monitoring
- ✅ Comprehensive logging
- ✅ Rate limiting support
- ✅ Docker containerization
- ✅ Full test coverage
- ✅ Production-ready code
- ✅ API documentation (Swagger)

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 📞 Support

For issues and questions:
1. Check existing issues on GitHub
2. Create detailed issue report
3. Include error logs and environment info

---

**Built with ❤️ using Python, React, and FastAPI**
