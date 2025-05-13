# Task Tracker API

A robust and scalable RESTful API built with FastAPI for efficient task and user management. This API provides a comprehensive solution for tracking tasks, managing users, and monitoring task progress in real-time.

## 🚀 Features

### User Management
- User registration and profile management
- Secure user authentication
- User listing and retrieval

### Task Management
- Create and assign tasks
- Real-time task status updates
- Task filtering and search capabilities
- User-specific task views

## 📋 API Endpoints

### User Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Welcome message and API status |
| POST   | `/users/`| Create a new user |
| GET    | `/users/`| Retrieve all users |

### Task Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/tasks/`| Create a new task |
| GET    | `/tasks/{task_id}` | Get specific task details |
| PUT    | `/tasks/{task_id}/status` | Update task status |
| GET    | `/users/{user_id}/tasks` | Get all tasks for a specific user |

## 🛠️ Technology Stack

- **Framework**: FastAPI
- **Python Version**: 3.8+
- **Documentation**: Swagger UI & ReDoc
- **Data Validation**: Pydantic
- **Server**: Uvicorn

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task-tracker-api
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Access the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📊 Data Models

### User Model
```python
{
    "id": int,
    "username": str,
    "email": str
}
```

### Task Model
```python
{
    "id": int,
    "title": str,
    "description": str,
    "status": TaskStatus,  # Enum: PENDING, IN_PROGRESS, COMPLETED
    "user_id": int,
    "created_at": datetime,
    "updated_at": datetime
}
```

## ⚠️ Error Handling

The API implements comprehensive error handling for various scenarios:
- 404: Resource not found
- 422: Invalid input data
- 500: Internal server error

## 🔒 Security

- Input validation using Pydantic models
- Secure data handling
- Error message sanitization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support, please open an issue in the repository or contact the maintainers.
