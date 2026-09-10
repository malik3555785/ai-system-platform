# Contributing to AI System Platform

## Development Setup

1. Clone the repository
```bash
git clone https://github.com/malik3555785/ai-system-platform.git
cd ai-system-platform
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Code Style

- Use Black for formatting: `black src/`
- Use isort for imports: `isort src/`
- Use flake8 for linting: `flake8 src/`
- Use mypy for type checking: `mypy src/`

## Testing

```bash
pytest tests/ -v --cov=src
```

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run tests and quality checks
4. Commit with clear message: `git commit -m "feat: description"`
5. Push and create pull request

## Issues

- Use clear, descriptive titles
- Include reproduction steps for bugs
- Suggest enhancements with use cases
