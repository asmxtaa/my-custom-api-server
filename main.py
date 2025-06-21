from fastapi import FastAPI, HTTPException
from models import Book, UpdateBook
import crud

app = FastAPI()

@app.post("/books")
def create(book: Book):
    return crud.create_book(book)

@app.get("/books")
def read_all():
    return crud.get_all_books()

@app.get("/books/{book_id}")
def read_one(book_id: str):
    try:
        return crud.get_book(book_id)
    except:
        raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update(book_id: str, book: UpdateBook):
    return crud.update_book(book_id, book)

@app.delete("/books/{book_id}")
def delete(book_id: str):
    if not crud.delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted"}
