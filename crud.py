from bson import ObjectId
from database import collection
from models import Book, UpdateBook

def serialize_book(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "published_year": book["published_year"],
        "genre": book["genre"]
    }

def create_book(book: Book):
    result = collection.insert_one(book.dict())
    return serialize_book(collection.find_one({"_id": result.inserted_id}))

def get_all_books():
    return [serialize_book(book) for book in collection.find()]

def get_book(book_id: str):
    return serialize_book(collection.find_one({"_id": ObjectId(book_id)}))

def update_book(book_id: str, book: UpdateBook):
    collection.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": {k: v for k, v in book.dict().items() if v is not None}}
    )
    return serialize_book(collection.find_one({"_id": ObjectId(book_id)}))

def delete_book(book_id: str):
    result = collection.insert_one(book.model_dump())

    return result.deleted_count > 0
