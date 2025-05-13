# FastAPI Pydantic Validation Examples

This project demonstrates various implementations of data validation using Pydantic models in FastAPI applications. It serves as a practical guide for implementing robust data validation in your FastAPI projects.

## 🚀 Features

- Basic model validation with type hints
- Field constraints and validation rules
- Optional fields and default values
- Custom validators
- Nested model validation
- Email validation
- Field constraints (min/max length, greater than, etc.)

## 📋 Prerequisites

- Python 3.8+
- FastAPI
- Pydantic
- Email-validator (for email validation)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Endpoints

1. **Create User** (`POST /create-user`)
   - Validates user data with email format
   - Required fields: name, age, email

2. **Create Product** (`POST /create-product`)
   - Validates product data with field constraints
   - Required fields: title (3-50 chars), price (>0), in_stock

3. **Create Blog** (`POST /create-blog`)
   - Demonstrates optional fields with default values
   - Required fields: title, content
   - Optional field: published (defaults to False)

4. **Create Employee** (`POST /create-employee`)
   - Shows custom validation implementation
   - Required fields: name, salary (must be positive)

5. **Create Customer** (`POST /create-customer`)
   - Demonstrates nested model validation
   - Required fields: name, email, address (street, city, zip_code)

## 📖 Documentation

- Interactive API documentation is available at `http://localhost:8000/docs`
- Alternative documentation at `http://localhost:8000/redoc`

## 🏗️ Project Structure

```
fastdca-p1/
├── main.py                 # Main application file
├── 01_basic_model_validation/  # Basic validation examples
├── 02_field_constraints/      # Field constraint examples
├── 03_nested_models/          # Nested model examples
├── pyproject.toml          # Project dependencies
└── README.md              # Project documentation
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

- Tahira Latif - Initial work

## 🙏 Acknowledgments

- FastAPI documentation
- Pydantic documentation 