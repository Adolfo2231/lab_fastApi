from fastapi.security import OAuth2PasswordBearer #? For OAuth2 authentication
from pydantic import BaseModel, Field
from schemas.users import User
"""Schemas for authentication"""

"""OAuth2 scheme for authentication"""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #? For OAuth2 authentication

# Login model
class Login(BaseModel):
    """Login model - only includes email and password"""
    email: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)

class LoginResponse(BaseModel):
    """Response model for login - only includes token"""
    token: str = Field(..., min_length=3, max_length=50)

class Register(BaseModel):
    """Register model - only includes public user data"""
    email: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=3, max_length=50)
    last_name: str = Field(..., min_length=3, max_length=50)

class RegisterResponse(BaseModel):
    """Response model for registration - only includes public user data"""
    email: str
    name: str
    last_name: str