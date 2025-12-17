from schemas.auth import Register, RegisterResponse
from utils.jwt import create_access_token, create_refresh_token
from utils.jwt import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS

class AuthService:
    """Service layer for authentication business logic"""
    
    @staticmethod
    def register_user(register_data: Register) -> RegisterResponse:
        """Register a new user"""
        user_dict = {
            "email": register_data.email,
            "username": register_data.username,
        }
        return user_dict
 
    @staticmethod
    def login_user(login_data: dict) -> dict:
        """Login a user"""
        # OAuth2 envía 'username', lo usamos directamente
        user = login_data.get("username")
        access_token = create_access_token({"sub": user})
        refresh_token = create_refresh_token({"sub": user})
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer", "access_token_expires_minutes": ACCESS_TOKEN_EXPIRE_MINUTES, "refresh_token_expires_days": REFRESH_TOKEN_EXPIRE_DAYS}