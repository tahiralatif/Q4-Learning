# 01 - Basic Model Validation (FastAPI + Pydantic)

This example demonstrates how to use **Pydantic** with **FastAPI** to perform basic data validation on incoming request bodies.

### ✅ Fields

| Field  | Type     | Validation                 |
|--------|----------|----------------------------|
| name   | `str`    | Required                   |
| age    | `int`    | Required                   |
| email  | `EmailStr` | Must be a valid email     |

### 🚀 How to Run

```bash
uvicorn main:app --reload
