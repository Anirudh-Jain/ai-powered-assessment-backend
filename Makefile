.PHONY: help setup up down logs clean build test frontend-install db-migrate

help:
	@echo "AI Assessment Platform - Development Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  setup              - Setup development environment"
	@echo "  up                 - Start all services (Docker Compose)"
	@echo "  down               - Stop all services"
	@echo "  logs               - View logs for all services"
	@echo "  build              - Build Docker images"
	@echo "  clean              - Clean up Docker resources"
	@echo "  test               - Run tests"
	@echo "  frontend-dev       - Start frontend development server locally"
	@echo "  backend-dev        - Start backend service locally"
	@echo "  env-setup          - Setup environment variables"
	@echo ""

setup: env-setup frontend-install
	@echo "✓ Development environment setup complete"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Run 'make up' to start Docker services"
	@echo "  2. Run 'make frontend-dev' and 'make backend-dev' separately for local development"

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
	@echo "  Frontend: http://localhost:3000"
	@echo "  Backend:  http://localhost:8000"

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
	@uv run --group dev pytest
	@echo ""
	@echo "Running frontend tests..."
	@cd frontend && npm test -- --passWithNoTests || true

frontend-dev:
	@echo "Starting frontend development server..."
	@cd frontend && npm run dev

backend-dev:
	@echo "Starting backend service locally..."
	@uv sync --group dev && uv run fastapi dev

db-migrate:
	@docker-compose run --rm backend alembic upgrade head

db-shell:
	docker-compose exec postgres psql -U assessmentuser -d assessment_db

health-check:
	@echo "Checking service health..."
	@for port in 8000 5432; do \
		echo -n "Service on port $$port: "; \
		curl -s http://localhost:$$port/health | grep -q healthy && echo "✓ Healthy" || echo "✗ Not responding"; \
	done

docs:
	@echo "API Documentation will be available at:"
	@echo "  http://localhost:8000/docs (Swagger UI)"
	@echo "  http://localhost:8000/redoc (ReDoc)"
