from fastapi import APIRouter, Depends
from schemas import User, UserPatch
from utils.jwt import get_current_user
from utils.role_verification import require_admin, require_premium, require_role

users_router = APIRouter()

# Example route with a required parameter (path parameter)
users = [User(name="John", last_name="Doe", age=30), User(name="Jane", last_name="Doe", age=25)]

@users_router.get("/all-users")
def get_all_users(current_user: dict = Depends(get_current_user)):
    """Route to get all users - requires authentication via Bearer token in Authorization header"""
    return {"message": "All users", "users": users, "current_user": current_user} #? Omits fields that are not in the User model like age

@users_router.post("/user")
def create_user(user: User):
    """Route to create a user"""
    return {"message": f"User created", "user": user}

@users_router.post("/welcome/{name}")
def saludar(name: str):
    """Route to greet with a required parameter"""
    return {"message": f"Hello {name}"}

@users_router.post("/welcome-default")
def saludar_default(name: str = "World"):
    """Route to greet with an optional parameter and a default value"""
    return {"message": f"Hello {name}"}

@users_router.put("/user/{id}")
def update_user_put(id: int, user: User):
    """Route to update a user with a request body"""
    return {"message": f"User {id} updated", "user": user}

@users_router.post("/welcome-body")
def saludar_body(body: User):
    """Route to greet with a request body"""
    return {"message": f"Hello {body.name} {body.last_name}"}

@users_router.patch("/user/{id}")
def update_user_patch(id: int, user: UserPatch):
    """Route to update a user"""
    return {"message": f"User {id} updated"}

@users_router.delete("/user/{id}")
def delete_user(id: int):
    """Route to delete a user"""
    return {"message": f"User {id} deleted"}

@users_router.get("/me/{id}")
def get_me(id: int, current_user: dict = Depends(get_current_user)):
    """Route to get the current user"""
    return {"message": f"User {id} ", "user": current_user}


# ============================================
# EJEMPLOS: Depends() con verificación de roles
# ============================================

@users_router.get("/admin-only")
def admin_only(admin_user: dict = Depends(require_admin)):
    """
    Ruta solo para administradores
    
    Esta ruta SOLO se ejecuta si require_admin() retorna el usuario
    Si el usuario no es admin, require_admin() lanza HTTPException(403)
    y esta función NUNCA se ejecuta
    """
    return {
        "mensaje": "Bienvenido al panel de administración",
        "usuario": admin_user.get("sub"),
        "acceso": "Solo administradores pueden ver esto"
    }


@users_router.get("/premium-content")
def premium_content(premium_user: dict = Depends(require_premium)):
    """
    Ruta solo para usuarios premium
    
    Esta ruta SOLO se ejecuta si require_premium() retorna el usuario
    Si el usuario no tiene premium, require_premium() lanza HTTPException(403)
    """
    return {
        "mensaje": "Contenido exclusivo para usuarios premium",
        "usuario": premium_user.get("sub"),
        "contenido": "Este es contenido premium exclusivo"
    }


@users_router.get("/moderator-content")
def moderator_content(mod_user: dict = Depends(require_role(["admin", "moderator"]))):
    """
    Ruta para administradores Y moderadores
    
    Usa require_role() con múltiples roles permitidos
    """
    return {
        "mensaje": "Contenido para moderadores y administradores",
        "usuario": mod_user.get("sub"),
        "acceso": "Tienes permisos de moderación"
    }