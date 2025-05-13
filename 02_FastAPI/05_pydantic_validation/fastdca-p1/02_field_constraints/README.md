# Field Constraints Validation

This example demonstrates how to implement field-level constraints and validations using Pydantic's Field class in FastAPI.

## 📝 Overview

This module shows how to:
- Add length constraints to string fields
- Set numeric range constraints
- Combine multiple validations
- Use Field class for advanced validation rules

## 🔍 Code Example

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., gt=17, lt=100)
    email: EmailStr

@app.post("/register")
def register_user(user: User):
    return {"message": "User registered", "data": user}
```

## 🎯 Features

1. **String Field Constraints**
   - `name`: Must be between 3 and 50 characters
   - Uses `min_length` and `max_length` validators

2. **Numeric Field Constraints**
   - `age`: Must be greater than 17 and less than 100
   - Uses `gt` (greater than) and `lt` (less than) validators

3. **Email Validation**
   - `email`: Must be a valid email format
   - Uses `EmailStr` type for validation

4. **API Endpoint**
   - Route: `POST /register`
   - Validates user data with all constraints
   - Returns success message and validated data

## 🚀 Testing the Endpoint

You can test this endpoint using curl or any API client:

```bash
curl -X POST "http://localhost:8000/register" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "John Doe",
           "age": 25,
           "email": "john@example.com"
         }'
```

### Valid Response Example:
```json
{
    "message": "User registered",
    "data": {
        "name": "John Doe",
        "age": 25,
        "email": "john@example.com"
    }
}
```

## ⚠️ Validation Rules

- `name`: 
  - Must be a string
  - Minimum length: 3 characters
  - Maximum length: 50 characters
- `age`:
  - Must be an integer
  - Must be greater than 17
  - Must be less than 100
- `email`:
  - Must be a valid email format

## 🔍 Common Field Validators

Here are some commonly used Field validators:
- `min_length`: Minimum length for strings
- `max_length`: Maximum length for strings
- `gt`: Greater than (for numbers)
- `lt`: Less than (for numbers)
- `ge`: Greater than or equal to
- `le`: Less than or equal to
- `regex`: Regular expression pattern
- `multiple_of`: Must be a multiple of this number

## 🔗 Related

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Field Documentation](https://pydantic-docs.helpmanual.io/usage/schema/#field-customization) 