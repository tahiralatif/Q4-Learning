# Nested Models Validation

This example demonstrates how to implement nested Pydantic models for complex data structures in FastAPI.

## 📝 Overview

This module shows how to:
- Create nested Pydantic models
- Validate complex data structures
- Handle hierarchical data validation
- Combine multiple models in a single request

## 🔍 Code Example

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Address(BaseModel):
    city: str
    country: str
    postal_code: str

class User(BaseModel):
    name: str
    email: EmailStr
    address: Address

@app.post("/register")
def register_user(user: User):
    return {
        "message": "User with address created",
        "data": user
    }
```

## 🎯 Features

1. **Nested Model Structure**
   - `User` model contains basic user information
   - `Address` model is nested within the User model
   - Each model has its own validation rules

2. **Model Components**
   - **User Model**:
     - `name`: String field for user's name
     - `email`: EmailStr field for valid email format
     - `address`: Nested Address model
   
   - **Address Model**:
     - `city`: String field for city name
     - `country`: String field for country name
     - `postal_code`: String field for postal code

3. **API Endpoint**
   - Route: `POST /register`
   - Validates complete user data including nested address
   - Returns success message and validated data

## 🚀 Testing the Endpoint

You can test this endpoint using curl or any API client:

```bash
curl -X POST "http://localhost:8000/register" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "John Doe",
           "email": "john@example.com",
           "address": {
               "city": "New York",
               "country": "USA",
               "postal_code": "10001"
           }
         }'
```

### Valid Response Example:
```json
{
    "message": "User with address created",
    "data": {
        "name": "John Doe",
        "email": "john@example.com",
        "address": {
            "city": "New York",
            "country": "USA",
            "postal_code": "10001"
        }
    }
}
```

## ⚠️ Validation Rules

- **User Model**:
  - `name`: Must be a string
  - `email`: Must be a valid email format
  - `address`: Must be a valid Address object

- **Address Model**:
  - `city`: Must be a string
  - `country`: Must be a string
  - `postal_code`: Must be a string

## 💡 Best Practices

1. **Model Organization**
   - Keep related fields together in separate models
   - Use meaningful model names
   - Maintain a clear hierarchy

2. **Validation**
   - Each nested model is validated independently
   - Parent model validation includes nested model validation
   - All validations must pass for the request to succeed

3. **Error Handling**
   - Validation errors will show the exact path to the invalid field
   - Nested model errors will include the full path (e.g., "address.city")

## 🔗 Related

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Nested Models Documentation](https://pydantic-docs.helpmanual.io/usage/models/#nested-models) 