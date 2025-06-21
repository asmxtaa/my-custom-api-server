from models import Book
from crud import create_book

def test_create_book():
    book_data = Book(title="Test Book", author="Tester", published_year=2025, genre="Test")
    result = create_book(book_data)
    assert result["title"] == "Test Book"
    assert "id" in result
