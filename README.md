# Lab FastAPI

FastAPI fundamentals lab - Educational project to learn the basics of FastAPI.

## 📋 Description

This project is a practical lab that demonstrates the fundamental concepts of FastAPI, including RESTful endpoint creation, data validation with Pydantic models, and automatic documentation. The project follows a modular architecture using FastAPI's `APIRouter` to organize endpoints by resource (users, auth, etc.), making it scalable and maintainable.

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
│   └── auth.py             # Authentication endpoints router (in development)
└── schemas/                # Pydantic data models
    ├── __init__.py
    └── schemas.py          # User and UserPatch models
```

## 📡 API Endpoints

### Users Endpoints (`/api/v1/users`)

- `GET /api/v1/users/all-users` - Get all users
- `POST /api/v1/users/user` - Create a new user
- `PUT /api/v1/users/user/{id}` - Update a user (full update)
- `PATCH /api/v1/users/user/{id}` - Update a user (partial update)
- `DELETE /api/v1/users/user/{id}` - Delete a user
- `POST /api/v1/users/welcome/{name}` - Greet with path parameter
- `POST /api/v1/users/welcome-default` - Greet with optional parameter
- `POST /api/v1/users/welcome-body` - Greet with request body

### Root Endpoint

- `GET /` - Root endpoint returning "Hello World"

## 🏛️ Architecture

The project uses a modular architecture with FastAPI routers:

- **Routers**: Each resource (users, auth) has its own router file in the `routes/` directory
- **Schemas**: Data models are defined in the `schemas/` directory using Pydantic
- **Main App**: The main FastAPI application (`main.py`) includes all routers with their respective prefixes and tags

```

## 🛠️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [Uvicorn](https://www.uvicorn.org/) - High-performance ASGI server
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation with types
