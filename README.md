# Lab FastAPI

FastAPI fundamentals lab - Educational project to learn the basics of FastAPI.

## 📋 Description

This project is a practical lab that demonstrates the fundamental concepts of FastAPI, including RESTful endpoint creation, data validation with Pydantic models, JWT authentication, and automatic documentation. The project follows a modular architecture using FastAPI's `APIRouter` to organize endpoints by resource (users, auth, etc.), with a service layer for business logic, making it scalable and maintainable.

## 🚀 Requirements

- Python 3.7 or higher
- pip (Python package manager)

## 📦 Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Running

To run the development server:

```bash
uvicorn main:app --reload
```

The server will be available at: `http://localhost:8000`

### Additional options:

```bash
# Specify custom port
uvicorn main:app --reload --port 5001

# Run without development mode
uvicorn main:app
```

## 📚 Documentation

FastAPI automatically generates interactive documentation. Once the server is running, access:

- **Swagger UI**: `http://localhost:8000/docs` - Complete interactive documentation
- **ReDoc**: `http://localhost:8000/redoc` - Alternative documentation
- **OpenAPI Schema**: `http://localhost:8000/openapi.json` - JSON schema

## 🏗️ Project Structure

```
lab_fastApi/
├── main.py                  # FastAPI main application
├── requirements.txt         # Project dependencies
├── README.md               # This file
├── routes/                 # API route modules
│   ├── __init__.py
│   ├── users.py            # User endpoints router
│   └── auth.py             # Authentication endpoints router
├── schemas/                # Pydantic data models
│   ├── __init__.py
│   ├── users.py            # User and UserPatch models
│   └── auth.py             # Login, Register, RegisterResponse, LoginResponse models
├── services/               # Business logic layer
│   └── auth_service.py     # Authentication service
├── utils/                  # Utility functions
│   ├── jwt.py              # JWT token creation and verification
│   └── role_verification.py # Role-based access control utilities
└── docs/                   # Documentation
    └── JWT_NOTES.md        # JWT documentation and notes
```

## 📡 API Endpoints

### Authentication Endpoints (`/api/v1/auth`)

- `POST /api/v1/auth/register` - Register a new user (returns user data without password)
- `POST /api/v1/auth/login` - Login with OAuth2 form data (username/password), receive access and refresh tokens
- `POST /api/v1/auth/logout` - Logout endpoint

### Users Endpoints (`/api/v1/users`)

**Public Endpoints:**
- `POST /api/v1/users/user` - Create a new user
- `POST /api/v1/users/welcome/{name}` - Greet with path parameter
- `POST /api/v1/users/welcome-default` - Greet with optional parameter
- `POST /api/v1/users/welcome-body` - Greet with request body

**Protected Endpoints (require authentication):**
- `GET /api/v1/users/all-users` - Get all users (requires Bearer token)
- `GET /api/v1/users/me/{id}` - Get current user info (requires Bearer token)
- `PUT /api/v1/users/user/{id}` - Update a user (full update)
- `PATCH /api/v1/users/user/{id}` - Update a user (partial update)
- `DELETE /api/v1/users/user/{id}` - Delete a user

**Role-Based Endpoints (require specific roles):**
- `GET /api/v1/users/admin-only` - Admin only access
- `GET /api/v1/users/premium-content` - Premium users only
- `GET /api/v1/users/moderator-content` - Moderators and admins only

### Root Endpoint

- `GET /` - Root endpoint returning "Hello World"

## 🏛️ Architecture

The project uses a modular architecture with FastAPI routers and a service layer:

- **Routers**: Each resource (users, auth) has its own router file in the `routes/` directory
- **Schemas**: Data models are defined in the `schemas/` directory using Pydantic (separated by domain: users, auth)
- **Services**: Business logic is handled in the `services/` directory, keeping routes thin
- **Utils**: Utility functions (JWT, etc.) are in the `utils/` directory
- **Main App**: The main FastAPI application (`main.py`) includes all routers with their respective prefixes and tags

### Flow Example (Register):

```
Client → Route (routes/auth.py) → Service (services/auth_service.py) → Route → Client
         (HTTP handling)          (Business logic)                    (Response formatting)
```


## 🔐 Authentication

The project implements JWT (JSON Web Token) authentication with OAuth2 password flow:

- **Token Creation**: Uses `python-jose` to create signed JWT tokens (access and refresh tokens)
- **Token Verification**: Tokens are verified on protected endpoints using `OAuth2PasswordBearer`
- **Token Structure**: Contains user identifier (`sub`), expiration (`exp`), and token type
- **Security**: 
  - Access tokens expire after 30 minutes by default
  - Refresh tokens expire after 7 days by default

### Using Authentication:

1. **Register**: `POST /api/v1/auth/register` with user data (email, username, password)
2. **Login**: `POST /api/v1/auth/login` with OAuth2 form data (username/password), receive:
   - `access_token`: JWT token for API access (expires in 30 minutes)
   - `refresh_token`: JWT token for refreshing access token (expires in 7 days)
   - `token_type`: "bearer"
   - `access_token_expires_minutes`: 30
   - `refresh_token_expires_days`: 7
3. **Use Token**: Include token in `Authorization: Bearer <access_token>` header for protected endpoints

### Swagger UI Authentication:

The login endpoint uses OAuth2 password flow. In Swagger UI:
1. Click "Authorize" button
2. Fill in username and password in the OAuth2 form
3. Click "Authorize" to get the token automatically
4. Protected endpoints will use the token automatically

## 🛠️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [Uvicorn](https://www.uvicorn.org/) - High-performance ASGI server
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation with types
