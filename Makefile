.PHONY: help setup up down logs clean build test frontend-install

help:
	@echo "AI Assessment Platform - Development Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  setup              - Setup development environment"
	@echo "  up                 - Start all services (Docker Compose)"
	@echo "  down               - Stop all services"
	@echo "  logs               - View logs from all services"
	@echo "  build              - Build Docker images"
	@echo "  clean              - Clean up Docker resources"
	@echo "  test               - Run tests for all services"
	@echo "  frontend-dev       - Start frontend development server locally"
	@echo "  backend-dev        - Start backend services locally"
	@echo "  env-setup          - Setup environment variables"
	@echo ""

setup: env-setup frontend-install
	@echo "✓ Development environment setup complete"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Run 'make up' to start Docker services"
	@echo "  2. Or run 'make frontend-dev' and 'make backend-dev' separately for local development"

env-setup:
	@if [ ! -f .env ]; then \
		cp .env.example .env 2>/dev/null || echo "# Create .env file with your configuration"; \
		echo "✓ Created .env file"; \
	else \
		echo "✓ .env file already exists"; \
	fi

frontend-install:
	@echo "Installing frontend dependencies..."
	@cd frontend && npm install

up:
	@echo "Starting all services..."
	docker-compose up -d
	@echo "✓ Services started"
	@echo ""
	@echo "Access points:"
	@echo "  Frontend:       http://localhost:3000"
	@echo "  API Gateway:    http://localhost:8000"
	@echo "  Auth Service:   http://localhost:8001"
	@echo "  Exam Service:   http://localhost:8002"
	@echo "  Question Service: http://localhost:8003"
	@echo "  Grading Service: http://localhost:8004"
	@echo "  Submission Service: http://localhost:8005"

down:
	@echo "Stopping services..."
	docker-compose down
	@echo "✓ Services stopped"

logs:
	docker-compose logs -f

build:
	@echo "Building Docker images..."
	docker-compose build
	@echo "✓ Build complete"

clean:
	@echo "Cleaning up Docker resources..."
	docker-compose down -v
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete
	@echo "✓ Cleanup complete"

test:
	@echo "Running backend tests..."
	@for service in auth exam question grading submission; do \
		echo "Testing $$service service..."; \
		cd services/$$service && pytest || true && cd ../..; \
	done
	@echo ""
	@echo "Running frontend tests..."
	@cd frontend && npm test -- --passWithNoTests || true

frontend-dev:
	@echo "Starting frontend development server..."
	@cd frontend && npm run dev

backend-dev:
	@echo "To run backend services locally:"
	@echo ""
	@echo "In separate terminals, run:"
	@for service in auth exam question grading submission api-gateway; do \
		echo "  cd services/$$service && uv venv && source .venv/bin/activate && uv pip install -r pyproject.toml && python main.py"; \
	done

db-shell:
	docker-compose exec postgres psql -U assessmentuser -d assessment_db

migration:
	@echo "Running database migrations..."
	docker-compose exec api-gateway alembic upgrade head

health-check:
	@echo "Checking service health..."
	@for port in 8000 8001 8002 8003 8004 8005; do \
		echo -n "Service on port $$port: "; \
		curl -s http://localhost:$$port/health | grep -q healthy && echo "✓ Healthy" || echo "✗ Not responding"; \
	done

docs:
	@echo "API Documentation will be available at:"
	@echo "  http://localhost:8000/docs (Swagger UI)"
	@echo "  http://localhost:8000/redoc (ReDoc)"
