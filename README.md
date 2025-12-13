# Lab FastAPI

FastAPI fundamentals lab - Educational project to learn the basics of FastAPI.

## 📋 Description

This project is a practical lab that demonstrates the fundamental concepts of FastAPI, including RESTful endpoint creation, data validation with Pydantic models, and automatic documentation.

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
lab_fastapi/
├── main.py              # FastAPI main application
├── schemas.py           # Pydantic models
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## 🛠️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [Uvicorn](https://www.uvicorn.org/) - High-performance ASGI server
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation with types
