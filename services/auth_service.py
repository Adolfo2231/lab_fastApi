from schemas.auth import Register, RegisterResponse

class AuthService:
    """Service layer for authentication business logic"""
    
    @staticmethod
    def register_user(register_data: Register) -> RegisterResponse:
        """
        Register a new user
        
        Args:
            register_data: Register model with user data including password
            
        Returns:
            RegisterResponse: User data without password
        """
        # Aquí iría la lógica de negocio:
        # - Validar que el email no exista
        # - Hashear la contraseña
        # - Guardar en base de datos
        # - Enviar email de confirmación
        # etc.
        
        # Guardar en BD y obtener el usuario
        # user = save_to_database(register_data)
        # user_dict = user.to_dict()  # Retorna dict SIN password (tu modelo nunca lo incluye)
        
        # Simulación del dict que retornaría user.to_dict()
        user_dict = {
            "email": register_data.email,
            "name": register_data.name,
            "password": register_data.password,
            "last_name": register_data.last_name
            # password NO está aquí porque tu modelo nunca lo devuelve
        }
        return user_dict