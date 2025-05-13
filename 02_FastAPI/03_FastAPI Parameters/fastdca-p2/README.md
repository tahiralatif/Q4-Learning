# fastdca-p2

A FastAPI project demonstrating the use of path and query parameters, Pydantic models, and basic CRUD operations. This project is ideal for learning how to build robust APIs with FastAPI and Python 3.11.

## Features
- FastAPI-based RESTful API
- Path and query parameter handling
- Pydantic model validation
- Basic CRUD endpoints
- Async request handling

## Requirements
- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn (for local development server)

## Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd fastdca-p2
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install fastapi pydantic uvicorn
   ```

## Usage
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

### Home
- **GET /**
  - Returns a welcome message.

### Get Item by ID
- **GET /items/{item_id}**
  - Path parameter: `item_id` (int, required, >=1)
  - Returns the item ID.

### Search Items
- **GET /items/**
  - Query parameter: `q` (str, optional)
  - Returns a search message or a default message if no query is provided.

### Get Item Details
- **GET /items/{item_id}/details**
  - Path parameter: `item_id` (int, required)
  - Query parameter: `detail` (str, optional)
  - Returns item details with or without the optional detail.

### Create Item
- **POST /items/**
  - Request body (JSON):
    ```json
    {
      "name": "string",
      "description": "string (optional)",
      "price": 0.0
    }
    ```
  - Returns the created item.

## Example Requests

**Create an item:**
```bash
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name": "Book", "description": "A novel", "price": 12.99}'
```

**Get item by ID:**
```bash
curl "http://127.0.0.1:8000/items/1"
```

**Search items:**
```bash
curl "http://127.0.0.1:8000/items/?q=phone"
```

## API Documentation
Interactive API docs are available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.
