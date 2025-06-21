# Book Manager API (FastAPI + MongoDB + Streamlit)

## Overview
This is a full-stack application with:
- FastAPI backend providing custom CRUD API endpoints
- MongoDB database for storing book data
- Streamlit frontend for user interaction

## Folder Structure
- `main.py`: FastAPI server
- `frontend.py`: Streamlit app
- `database.py`: MongoDB connection
- `models.py`: Pydantic schemas
- `crud.py`: Business logic
- `.env.example`: Sample environment variables
- `requirements.txt`: Dependencies
- `tests/`: Unit and integration tests

## 🔗 API Endpoints
| Method | Endpoint         | Description      |
|--------|------------------|------------------|
| POST   | `/books`         | Add a new book   |
| GET    | `/books`         | View all books   |
| GET    | `/books/{id}`    | Get book by ID   |
| PUT    | `/books/{id}`    | Update book      |
| DELETE | `/books/{id}`    | Delete book      |

## How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/asmxtaa/my-custom-api-server.git
cd my-custom-api-server
```

2. Set Up Environment
```bash
python -m venv venv
source venv/Scripts/activate  # For Windows PowerShell or Git Bash
pip install -r requirements.txt
```

3. Add .env File
Create a .env file in the root folder with:

```ini
MONGO_URI=mongodb://localhost:27017
DB_NAME=myapi_db
```

4. Run FastAPI Server
```bash
uvicorn main:app --reload
```

5. Run Streamlit Frontend
```bash
streamlit run frontend.py
```
Open: http://localhost:8501

## Testing
### Run Tests
```bash
pytest --cov=.
```

### Test Coverage Report
View coverage report after tests run by opening htmlcov/index.html (generate with pytest --cov=. --cov-report=html).

We use:

- pytest for testing
- pytest-cov for coverage
- mongomock for mocking MongoDB in unit tests

## Tech Stack
- Python 3.10+
- FastAPI
- MongoDB
- Pydantic
- Streamlit
- pytest & pytest-cov
- mongomock

## Test Coverage Snapshot
![Coverage Report](./coverage.png)


## License
MIT License
