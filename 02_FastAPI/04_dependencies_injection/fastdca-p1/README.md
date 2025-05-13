# fastdca-p1

A FastAPI project demonstrating advanced dependency injection patterns, including parameterized dependencies, login checks, and custom 404 handling.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [License](#license)

## Overview
This project showcases how to use FastAPI's dependency injection system for building robust, modular APIs. It includes examples of simple and parameterized dependencies, login validation, combining multiple dependencies, and custom 404 error handling.

## Features
- Simple and parameterized dependency injection
- Login validation using query parameters
- Combining multiple dependencies in a single endpoint
- Custom 404 error handling for resource fetching
- Type-annotated endpoints for clarity and validation

## Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd fastdca-p1
   ```
2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Unix or MacOS:
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or, if using pyproject.toml:
   pip install .
   ```

## Usage
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

Interactive API docs are available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints
| Method | Endpoint         | Description                                  |
|--------|------------------|----------------------------------------------|
| GET    | `/goal`          | Returns a static goal message                |
| GET    | `/user-goal`     | Returns a goal message with a username param |
| GET    | `/login`         | Validates login with `username` and `password` query params |
| GET    | `/sum/{num}`     | Returns the sum of `num`, `num+1`, and `num+2` |
| GET    | `/blog/{id}`     | Fetches a blog by ID or returns 404          |
| GET    | `/user/{id}`     | Fetches a user by ID or returns 404          |

## Project Structure
```
fastdca-p1/
├── main.py         # FastAPI application with endpoints and dependencies
├── pyproject.toml  # Project metadata and dependencies
├── uv.lock         # Lock file for reproducible installs
├── README.md       # Project documentation
└── .venv/          # (Optional) Virtual environment
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
