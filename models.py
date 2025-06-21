from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    published_year: int
    genre: str

class UpdateBook(BaseModel):
    title: Optional[str]
    author: Optional[str]
    published_year: Optional[int]
    genre: Optional[str]
