from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import date, datetime
from enum import Enum

# Enum for task status
class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

# User schemas
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True  # ✅ Pydantic v2 replacement for orm_mode

# Task schemas
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    status: TaskStatus = TaskStatus.pending
    user_id: int

    @field_validator('due_date')
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date cannot be in the past.")
        return v

class TaskRead(TaskCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  
