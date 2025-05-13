from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

# ===== 1. Simple Model Validation =====
class User(BaseModel):
    name: str
    age: int
    email: EmailStr

@app.post("/create-user")
def create_user(user: User):
    return {"message": "User created successfully", "data": user}


# ===== 2. Add Field Validation (min, max) =====
class Product(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    in_stock: bool

@app.post("/create-product")
def create_product(product: Product):
    return {"message": "Product created successfully", "data": product}


# ===== 3. Optional Fields and Default Values =====
from typing import Optional

class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool] = False

@app.post("/create-blog")
def create_blog(blog: Blog):
    return {"message": "Blog created successfully", "data": blog}


# ===== 4. Custom Validator (Example) =====
from pydantic import validator

class Employee(BaseModel):
    name: str
    salary: float

    @validator('salary')
    def salary_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Salary must be greater than 0')
        return v

@app.post("/create-employee")
def create_employee(employee: Employee):
    return {"message": "Employee created successfully", "data": employee}


# ===== 5. Nested Models =====
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Customer(BaseModel):
    name: str
    email: EmailStr
    address: Address

@app.post("/create-customer")
def create_customer(customer: Customer):
    return {"message": "Customer created successfully", "data": customer}
