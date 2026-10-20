from fastapi import APIRouter

from src.schemas.auth import UserLogin, UserRegister

router = APIRouter()


@router.post("/register")
async def register(user: UserRegister):
    return {
        "access_token": "mock-token",
        "token_type": "bearer",
        "user_id": "mock-user-id",
    }


@router.post("/login")
async def login(credentials: UserLogin):
    return {
        "access_token": "mock-token",
        "token_type": "bearer",
        "user_id": "mock-user-id",
    }


@router.get("/validate")
async def validate_token(token: str):
    return {"valid": True, "user_id": "mock-user-id"}
