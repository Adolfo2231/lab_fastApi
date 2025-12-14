from pydantic import BaseModel, Field
from typing import Optional

"""
Schemas are the data models that will be used in the API.
"""

# User model
class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    last_name: str = Field(..., min_length=3, max_length=50)

# User model for partial update
class UserPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    last_name: Optional[str] = Field(None, min_length=3, max_length=50)