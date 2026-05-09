# AI Powered Assessment & Examination Platform

A microservices-based platform for creating, taking, and auto-grading exams using AI technology.

## Architecture

The platform uses a microservices architecture with the following components:

- **Frontend**: Next.js 16+ with React Server Components (TypeScript, Tailwind CSS)
- **API Gateway**: FastAPI service routing requests to microservices
- **Auth Service**: User authentication and JWT token management
- **Exam Service**: Exam creation, management, and participant tracking
- **Question Service**: Question management and AI-powered question generation
- **Grading Service**: AI-powered auto-grading and feedback generation
- **Submission Service**: Exam submission tracking and result management
- **Database**: PostgreSQL for data persistence

## Tech Stack

- **Frontend**: Next.js 16+, React 19, TypeScript, Tailwind CSS
- **Backend**: FastAPI 0.115+, Python 3.11+, uv (package manager)
- **Database**: PostgreSQL 16
- **AI**: OpenAI API for question generation and auto-grading
- **Containerization**: Docker, Docker Compose

## Project Structure

```
.
├── frontend/                 # Next.js 16+ frontend application
├── services/
│   ├── api-gateway/         # API Gateway (FastAPI)
│   ├── auth/                # Authentication Service
│   ├── exam/                # Exam Management Service
│   ├── question/            # Question Management & AI Generation
│   ├── grading/             # AI-powered Grading Service
│   └── submission/          # Submission Tracking Service
├── docker-compose.yml       # Docker Compose orchestration
├── .env                     # Environment variables
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Prerequisites

- Docker and Docker Compose
- Node.js 20+ (for local frontend development)
- Python 3.11+ (for local backend development)
- uv package manager (for Python dependency management)
- OpenAI API key (for AI features)

## Quick Start

### Using Docker Compose (Recommended)

1. **Clone and setup**:
```bash
cd AI-Assessment-Platform
cp .env.example .env
# Edit .env and add your OpenAI API key
```

2. **Start all services**:
```bash
docker-compose up -d
```

3. **Verify services are running**:
```bash
curl http://localhost:8000/health     # API Gateway
curl http://localhost:8001/health     # Auth Service
curl http://localhost:8002/health     # Exam Service
curl http://localhost:8003/health     # Question Service
curl http://localhost:8004/health     # Grading Service
curl http://localhost:8005/health     # Submission Service
```

4. **Access the frontend**:
Open http://localhost:3000 in your browser

### Local Development Setup

#### Frontend

```bash
cd frontend
npm install
npm run dev
# Runs on http://localhost:3000
```

#### Backend Services

For each service (auth, exam, question, grading, submission):

```bash
cd services/{service-name}
uv venv                    # Create virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml
python main.py
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get JWT token

### Exams
- `GET /api/exams` - List all exams
- `POST /api/exams` - Create a new exam
- `GET /api/exams/{exam_id}` - Get exam details

### Questions
- `GET /api/questions` - List questions
- `POST /api/questions` - Create a question
- `POST /api/questions/generate` - Generate AI questions

### Submissions
- `POST /api/submissions` - Submit exam answers
- `GET /api/submissions` - Get submission history

### Grading
- `POST /api/grade` - Grade a submission
- `GET /api/grades/{submission_id}` - Get grades for submission

## Environment Variables

Create a `.env` file in the root directory:

```env
# OpenAI Configuration
OPENAI_API_KEY=your-key-here

# Database
DATABASE_URL=postgresql://user:password@postgres:5432/assessment_db

# JWT
JWT_SECRET=your-secret-key

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Development Workflow

1. **Create a feature branch**:
```bash
git checkout -b feature/your-feature
```

2. **Make changes and test locally**:
```bash
# Start all services
docker-compose up

# OR run services individually for development
```

3. **Run tests**:
```bash
# Backend tests
cd services/{service-name}
pytest

# Frontend tests
cd frontend
npm test
```

4. **Commit and push**:
```bash
git add .
git commit -m "Add feature description"
git push origin feature/your-feature
```

## Deployment

### Deploy to Production

1. **Set production environment variables**:
```bash
export OPENAI_API_KEY=your-production-key
export JWT_SECRET=your-production-secret
export DATABASE_URL=production-database-url
```

2. **Build and push Docker images**:
```bash
docker-compose build
docker tag <service> your-registry/<service>:latest
docker push your-registry/<service>:latest
```

3. **Deploy using Docker Swarm or Kubernetes**:
- Frontend: Deploy to Vercel
- Backend: Deploy to Railway, Heroku, or any container platform
- Database: Use managed PostgreSQL service

## Features

### Implemented
- [ ] User authentication (JWT)
- [ ] Exam CRUD operations
- [ ] AI question generation
- [ ] Exam submission tracking
- [ ] AI-powered auto-grading

### Roadmap
- [ ] Role-based access control (RBAC)
- [ ] Exam analytics and reporting
- [ ] Question bank management
- [ ] Proctoring features
- [ ] Mobile app

## Testing

### Backend Unit Tests
```bash
cd services/{service-name}
pytest tests/
```

### Integration Tests
```bash
pytest tests/integration/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Performance Optimization

- Database connection pooling
- Caching layer (Redis - future)
- API rate limiting
- Request validation and error handling
- Async/await for I/O operations

## Security Considerations

For production deployment:
- Use HTTPS/TLS
- Implement API authentication with OAuth2
- Use secrets management (AWS Secrets Manager, Vault)
- Implement rate limiting and DDoS protection
- Regular security audits
- Input validation and sanitization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License

## Support

For issues and questions:
- Create an issue in the GitHub repository
- Contact the development team

## Authors

- Your Name
- Development Team

## Acknowledgments

- FastAPI documentation
- Next.js documentation
- OpenAI API documentation
