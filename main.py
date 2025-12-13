from fastapi import FastAPI
from schemas import User, UserPatch

"""FastAPI fundamentals lab - Educational project to learn the basics of FastAPI."""

# Create the FastAPI application
app = FastAPI()

@app.get("/")
def read_root():
    """Route for the main page"""
    return {"message": "Hello World"}

# Example route with a required parameter (path parameter)
users = [User(name="John", last_name="Doe", age=30), User(name="Jane", last_name="Doe", age=25)]

@app.get("/all-users")
def get_all_users():
    """Route to get all users"""
    return {"message": "All users", "users": users} #? Omits fields that are not in the User model like age

@app.post("/user")
def create_user(user: User):
    """Route to create a user"""
    return {"message": f"User created", "user": user}

@app.post("/welcome/{name}")
def saludar(name: str):
    """Route to greet with a required parameter"""
    return {"message": f"Hello {name}"}

@app.post("/welcome-default")
def saludar_default(name: str = "World"):
    """Route to greet with an optional parameter and a default value"""
    return {"message": f"Hello {name}"}

@app.put("/user/{id}")
def update_user_put(id: int, user: User):
    """Route to update a user with a request body"""
    return {"message": f"User {id} updated", "user": user}

@app.post("/welcome-body")
def saludar_body(body: User):
    """Route to greet with a request body"""
    return {"message": f"Hello {body.name} {body.last_name}"}

@app.patch("/user/{id}")
def update_user_patch(id: int, user: UserPatch):
    """Route to update a user"""
    return {"message": f"User {id} updated"}

@app.delete("/user/{id}")
def delete_user(id: int):
    """Route to delete a user"""
    return {"message": f"User {id} deleted"}
