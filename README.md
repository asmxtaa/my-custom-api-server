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
- `.env.example`: Safe sample env file
- `requirements.txt`: Dependencies

## 🔗 API Endpoints
| Method | Endpoint         | Description      |
|--------|------------------|------------------|
| POST   | `/books`         | Add a new book   |
| GET    | `/books`         | View all books   |
| GET    | `/books/{id}`    | Get book by ID   |
| PUT    | `/books/{id}`    | Update book      |
| DELETE | `/books/{id}`    | Delete book      |

##  How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/my-custom-api-server.git
cd my-custom-api-server
```

### 2. Set Up Environment
```bash
python -m venv venv
source venv/Scripts/activate  # or venv/bin/activate on Mac/Linux
pip install -r requirements.txt
```

### 3. Add `.env` File
Create a `.env` file with:
```env
MONGO_URI=mongodb://localhost:27017
DB_NAME=myapi_db
```

### 4. Run FastAPI Server
```bash
uvicorn main:app --reload
```

### 5. Run Streamlit Frontend
```bash
streamlit run frontend.py
```

Open your browser at: [http://localhost:8501](http://localhost:8501)
