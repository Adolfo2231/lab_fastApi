from fastapi import FastAPI
from routes.users import users_router
from routes.auth import auth_router
# Lab routers - comentados por ahora (solo para aprendizaje local)
# from routes.lab_depends import lab_router
# from routes.lab_query_demo import query_demo_router

"""FastAPI fundamentals lab - Educational project to learn the basics of FastAPI."""

# Create the FastAPI application
app = FastAPI()

@app.get("/")
def read_root():
    """Route for the main page"""
    return {"message": "Hello World"}

# Include routers with their prefixes
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["authentication"])
# Lab routers - comentados por ahora (solo para aprendizaje local)
# app.include_router(lab_router, prefix="/lab/depends", tags=["lab-depends"])
# app.include_router(query_demo_router, prefix="/lab/query", tags=["lab-query"])