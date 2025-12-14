from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from jose import jwt

# Configuración JWT
SECRET_KEY = "change-this-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_token(data, expire_delta):

    #* 1. Copiamos los datos que queremos meter en el token
    #? Copiamos los datos para crear capa de seguridad, asi no se modifica el original
    to_encode = data.copy()

    #* 2 Calculamos la expiracion
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    #!3 agregamos el claim obligatorio "exp"
    #? Sin esto el token no expira nunca brecha de seguridad
    to_encode.update({"exp": expire})

    #* 4. Creamos y firmamos el token
    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

if __name__ == "__main__":
    data = {"sub": "user@email.com", "role": "admin"}
    expire_delta = timedelta(hours=1)
    token = create_token(data, expire_delta)
    print(f"Token de 1 hora: {token}")
    
    # Decodificar para ver el payload
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    print(f"Expira en: {payload.get('exp')} (timestamp)")
    print(f"Usuario: {payload.get('sub')} Role: {payload.get('role')}")
    print(f"Expira en: {datetime.fromtimestamp(payload.get('exp'))} (fecha legible)\n")

    data2 = {"sub": "user2@email.com"}
    expire_delta2 = timedelta(days=7)
    token2 = create_token(data2, expire_delta2)
    print(f"Token de 7 dias: {token2}")
    
    # Decodificar para ver el payload
    payload2 = jwt.decode(token2, SECRET_KEY, algorithms=[ALGORITHM])
    print(f"Expira en: {payload2.get('exp')} (timestamp)") #? .get('exp') es para obtener el timestamp de la expiracion Ej: 1718313600
    print(f"Usuario: {payload2.get('sub')} Role: {payload2.get('role')}") #? .get('sub') es para obtener el usuario Ej: user2@email.com
    print(f"Expira en: {datetime.fromtimestamp(payload2.get('exp'))} (fecha legible)") #? .fromtimestamp es para convertir el timestamp a fecha legible
