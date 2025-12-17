from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth import Register, RegisterResponse, LoginResponse
from services.auth_service import AuthService

auth_router = APIRouter()

@auth_router.post("/register", response_model=RegisterResponse)
def register(register: Register) -> RegisterResponse:
    """Route to register - receives Register model and returns RegisterResponse without password"""
    user = AuthService.register_user(register)
    return RegisterResponse(**user)

@auth_router.post("/login", response_model=LoginResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Route to login - accepts OAuth2 form data (username/password)
    OAuth2'
    """

    login_data = {"username": form_data.username, "password": form_data.password}
    token_dict = AuthService.login_user(login_data)
    # Retornar LoginResponse para que Swagger muestre el schema correcto
    return LoginResponse(**token_dict)

@auth_router.post("/logout")
def logout():
    """Route to logout"""
    return {"message": "Logout endpoint"}