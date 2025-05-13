from fastapi import FastAPI, Depends, Query, HTTPException, status
from typing import Annotated

app = FastAPI()

# ===== 1. Simple Dependency =====
def provide_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/goal")
def show_goal(data: Annotated[dict, Depends(provide_goal)]):
    return data


# ===== 2. Dependency with Parameter =====
def user_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "user": username}

@app.get("/user-goal")
def show_user_goal(data: Annotated[dict, Depends(user_goal)]):
    return data


# ===== 3. Login Dependency =====
def check_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    return {"message": "Login Failed"}

@app.get("/login")
def login_status(data: Annotated[dict, Depends(check_login)]):
    return data


# ===== 4. Multiple Dependencies =====
def add_one(num: int):
    return num + 1

def add_two(num: int):
    return num + 2

@app.get("/sum/{num}")
def show_sum(num: int, res1: Annotated[int, Depends(add_one)], res2: Annotated[int, Depends(add_two)]):
    total = num + res1 + res2
    return {"result": total}


# ===== 5. Fetch Object or 404 =====
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

class FetchOr404:
    def __init__(self, data):
        self.data = data

    def __call__(self, id: str):
        item = self.data.get(id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID {id} not found")
        return item

fetch_blog = FetchOr404(blogs)
fetch_user = FetchOr404(users)

@app.get("/blog/{id}")
def show_blog(blog: Annotated[str, Depends(fetch_blog)]):
    return {"blog": blog}

@app.get("/user/{id}")
def show_user(user: Annotated[str, Depends(fetch_user)]):
    return {"user": user}

