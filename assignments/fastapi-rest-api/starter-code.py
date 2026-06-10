"""
FastAPI Book Management API - Starter Code

This is the foundation for building a complete REST API for managing a book collection.
Your task is to implement all endpoints and functionality as described in the assignment.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(
    title="Book Management API",
    description="A simple REST API for managing a book collection",
    version="1.0.0"
)

# Define the Book data model
class Book(BaseModel):
    """
    Book model for the API.
    
    Attributes:
        id: Unique identifier for the book
        title: Title of the book
        author: Author of the book
        year: Publication year
        description: Brief description of the book
    """
    id: int
    title: str
    author: str
    year: int
    description: Optional[str] = None


# In-memory storage for books (use a list or dictionary)
books_db: List[Book] = [
    Book(
        id=1,
        title="Python Programming",
        author="John Doe",
        year=2020,
        description="Learn Python from basics to advanced concepts"
    ),
    Book(
        id=2,
        title="Web Development with FastAPI",
        author="Jane Smith",
        year=2023,
        description="Build modern web APIs with FastAPI and Python"
    )
]


# TODO: Implement GET /books endpoint
# Should return all books in the collection
@app.get("/books", response_model=List[Book])
async def get_all_books():
    """Get all books in the collection."""
    pass


# TODO: Implement GET /books/{book_id} endpoint
# Should return a specific book by ID, or 404 if not found
@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Get a specific book by ID."""
    pass


# TODO: Implement POST /books endpoint
# Should create a new book and return it with 201 status code
@app.post("/books", response_model=Book, status_code=201)
async def create_book(book: Book):
    """Create a new book in the collection."""
    pass


# TODO: Implement PUT /books/{book_id} endpoint
# Should update an existing book or return 404 if not found
@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_data: Book):
    """Update an existing book."""
    pass


# TODO: Implement DELETE /books/{book_id} endpoint
# Should delete a book and return 204 No Content, or 404 if not found
@app.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int):
    """Delete a book from the collection."""
    pass


# TODO: Create test_api.py file with test cases
# Test at least 5 different scenarios covering all CRUD operations


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
