from pydantic import BaseModel, Field

"""Schemas for authentication"""

# Login model
class Login(BaseModel):
    """Login model - only includes email and password"""
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)

class LoginResponse(BaseModel):
    """Response model for login - only includes token"""
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")
    access_token_expires_minutes: int = Field(..., description="Token expiration time in minutes")
    refresh_token: str = Field(..., description="JWT refresh token")
    refresh_token_expires_days: int = Field(..., description="Refresh token expiration time in days")

class Register(BaseModel):
    """Register model - only includes public user data"""
    email: str = Field(..., min_length=3, max_length=50)
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)

class RegisterResponse(BaseModel):
    """Response model for registration - only includes public user data"""
    email: str
    username: str