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
