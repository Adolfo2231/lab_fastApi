from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

# Configuración JWT
SECRET_KEY = "change-this-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# HTTPBearer scheme para extraer el token del header Authorization: Bearer <token>
# Esto hace que Swagger UI solo pida el token directamente, sin formulario OAuth2
#security = HTTPBearer()

# OAuth2 scheme para extraer el token del header Authorization: Bearer <token>
# tokenUrl debe coincidir con la ruta de login (sin el prefijo del router)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def create_access_token(data, expire_delta: Optional[timedelta] = None) -> str:

    #* 1. Copiamos los datos que queremos meter en el token
    #? Copiamos los datos para crear capa de seguridad, asi no se modifica el original
    to_encode = data.copy()

    #* 2 Calculamos la expiracion
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    #!3 agregamos el claim obligatorio "exp" y el tipo de token
    #? Sin esto el token no expira nunca brecha de seguridad
    #? El "type" debe ir dentro del payload, no como parámetro de jwt.encode()
    to_encode.update({"exp": expire, "type": "access"})

    #* 4. Creamos y firmamos el token
    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

def create_refresh_token(data, expire_delta: Optional[timedelta] = None) -> str:
    """Create a refresh token"""
   
    to_encode = data.copy()
   
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    to_encode.update({"exp": expire, "type": "refresh"})

    token = jwt.encode(
        to_encode,
        SECRET_KEY, 
        algorithm=ALGORITHM
    )
    return token


def verify_token(token: str) -> Dict[str, Any]:
    """
    Verifica y decodifica un token JWT
    
    Paso a paso:
    1. Recibe el token (string con formato: header.payload.signature)
    2. Intenta decodificar usando jwt.decode()
    3. jwt.decode() internamente:
       a. Separa el token en sus 3 partes (header, payload, signature)
       b. Decodifica el header (verifica algoritmo)
       c. Decodifica el payload (obtiene los datos)
       d. Recalcula la firma usando SECRET_KEY y ALGORITHM
       e. Compara la firma recalculada con la firma del token
       f. Si las firmas coinciden → token válido
       g. Verifica que el token no haya expirado (compara 'exp' con fecha actual)
    4. Si todo es válido, retorna el payload (dict con los datos)
    5. Si algo falla, lanza JWTError
    """
    
    #* 1. Intentamos decodificar el token
    #? jwt.decode() hace múltiples verificaciones automáticamente:
    #? - Verifica que la firma sea válida (usando SECRET_KEY)
    #? - Verifica que el algoritmo sea el correcto (ALGORITHM)
    #? - Verifica que el token no haya expirado (compara 'exp' con ahora)
    try:
        payload = jwt.decode(
            token,                    # Token a verificar (string completo)
            SECRET_KEY,               # MISMA clave usada para crear el token
            algorithms=[ALGORITHM]    # MISMO algoritmo usado para crear el token
        )
        
        #* 2. Si llegamos aquí, el token es válido
        #? jwt.decode() ya verificó:
        #? ✅ Firma correcta
        #? ✅ Algoritmo correcto
        #? ✅ Token no expirado
        return payload
        
    except JWTError as e:
        #* 3. Si algo falla, jwt.decode() lanza JWTError
        #? Puede ser por:
        #? - Token expirado (ExpiredSignatureError)
        #? - Firma inválida (InvalidSignatureError)
        #? - Token malformado (DecodeError)
        #? - Algoritmo incorrecto
        #? - SECRET_KEY incorrecta
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Dependencia de FastAPI para proteger rutas con autenticación JWT
    
    Extrae el token del header Authorization: Bearer <token>
    y valida que sea un token válido.
    """
    payload = verify_token(token)
    return payload

if __name__ == "__main__":
    # Ejemplo: Crear token
    data = {"sub": "user@email.com", "role": "admin"}
    expire_delta = timedelta(hours=1)
    token = create_access_token(data, expire_delta)
    print(f"Token de 1 hora: {token}")
    
    # Ejemplo: Verificar token
    payload = verify_token(token)
    print(f"Payload: {payload}")
    print(f"Expira en: {payload.get('exp')} (timestamp)")
    print(f"Usuario: {payload.get('sub')} Role: {payload.get('role')}")
    print(f"Expira en: {datetime.fromtimestamp(payload.get('exp'))} (fecha legible)\n")

    # Ejemplo: Token con diferente expiración
    data2 = {"sub": "user2@email.com"}
    expire_delta2 = timedelta(days=7)
    token2 = create_access_token(data2, expire_delta2)
    print(f"Token de 7 dias: {token2}")
    
    # Verificar segundo token
    payload2 = verify_token(token2)
    print(f"Expira en: {payload2.get('exp')} (timestamp)") #? .get('exp') es para obtener el timestamp de la expiracion Ej: 1718313600
    print(f"Usuario: {payload2.get('sub')} Role: {payload2.get('role')}") #? .get('sub') es para obtener el usuario Ej: user2@email.com
    print(f"Expira en: {datetime.fromtimestamp(payload2.get('exp'))} (fecha legible)") #? .fromtimestamp es para convertir el timestamp a fecha legible
