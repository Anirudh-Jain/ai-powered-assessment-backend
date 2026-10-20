from pydantic import BaseModel


class UserRegister(BaseModel):
    email: str
    password: str
    full_name: str
    role: str


class UserLogin(BaseModel):
    email: str
    password: str
