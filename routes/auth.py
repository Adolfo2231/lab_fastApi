from fastapi import APIRouter
from schemas.auth import Login, Register, RegisterResponse
from services.auth_service import AuthService

auth_router = APIRouter()

@auth_router.post("/login")
def login(login: Login):
    """Route to login - receives credentials and returns token"""
    return {"message": "Login endpoint", "token": "fake_token_for_now"}


@auth_router.post("/logout")
def logout():
    """Route to logout"""
    return {"message": "Logout endpoint"}


@auth_router.post("/register", response_model=RegisterResponse)
def register(register: Register) -> RegisterResponse:
    """
    Route to register - receives Register model and returns RegisterResponse without password
    """
    user = AuthService.register_user(register)
    return RegisterResponse(**user)

