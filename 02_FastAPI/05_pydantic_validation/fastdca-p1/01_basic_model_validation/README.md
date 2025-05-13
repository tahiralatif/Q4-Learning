# Basic Model Validation

This example demonstrates the fundamental usage of Pydantic models for data validation in FastAPI.

## 📝 Overview

This module shows how to:
- Create a basic Pydantic model
- Use type hints for validation
- Implement email validation
- Handle basic data validation in FastAPI endpoints

## 🔍 Code Example

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

@app.post("/create-user")
def create_user(user: User):
    return {"message": "User created successfully", "data": user}
```

## 🎯 Features

1. **Type Validation**
   - `name`: Must be a string
   - `age`: Must be an integer
   - `email`: Must be a valid email format (using EmailStr)

2. **API Endpoint**
   - Route: `POST /create-user`
   - Validates incoming user data against the User model
   - Returns success message and validated data

## 🚀 Testing the Endpoint

You can test this endpoint using curl or any API client:

```bash
curl -X POST "http://localhost:8000/create-user" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "John Doe",
           "age": 30,
           "email": "john@example.com"
         }'
```

### Valid Response Example:
```json
{
    "message": "User created successfully",
    "data": {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com"
    }
}
```

## ⚠️ Validation Rules

- All fields are required by default
- `name` must be a string
- `age` must be an integer
- `email` must be a valid email format

## 🔗 Related

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/) 