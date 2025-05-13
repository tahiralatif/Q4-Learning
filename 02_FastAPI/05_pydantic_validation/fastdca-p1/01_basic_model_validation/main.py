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
