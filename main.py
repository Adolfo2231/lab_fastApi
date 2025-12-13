from fastapi import FastAPI
from routes.users import users_router

"""FastAPI fundamentals lab - Educational project to learn the basics of FastAPI."""

# Create the FastAPI application
app = FastAPI()

@app.get("/")
def read_root():
    """Route for the main page"""
    return {"message": "Hello World"}

# Include routers with their prefixes
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])