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
# This code defines a FastAPI application with a nested Pydantic model for user registration.
# The `User` model contains an `Address` model, which is used to validate the address information.