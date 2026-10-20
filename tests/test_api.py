from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "backend"}


def test_create_exam_response_contract():
    response = client.post(
        "/exams",
        json={
            "title": "Algebra",
            "description": "Linear equations",
            "duration_minutes": 45,
            "total_questions": 8,
            "pass_percentage": 60,
            "created_by": "teacher-1",
        },
    )

    assert response.status_code == 200
    assert response.json()["id"] == "mock-exam-id"
    assert response.json()["title"] == "Algebra"
    assert response.json()["created_by"] == "teacher-1"


def test_domain_routes_are_registered():
    route_paths = set(app.openapi()["paths"])

    assert {
        "/register",
        "/exams",
        "/questions",
        "/submissions",
        "/grade",
    } <= route_paths
