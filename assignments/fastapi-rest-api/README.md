# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a modern, production-ready REST API using the FastAPI framework. You'll create a complete CRUD (Create, Read, Update, Delete) API for managing a book collection, complete with data validation, error handling, and interactive API documentation.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project and Create Base API

#### Description

Initialize a FastAPI project and create the basic structure for a Book Management API. You'll set up the application, define data models, and create your first endpoints.

#### Requirements

Your project should:

- Install FastAPI and Uvicorn dependencies
- Create a `main.py` file that initializes the FastAPI application
- Define a `Book` data model using Pydantic with fields: `id`, `title`, `author`, `year`, and `description`
- Implement a GET endpoint (`/books`) that returns all books in the collection
- Implement a GET endpoint (`/books/{book_id}`) that returns a specific book by ID
- Include proper HTTP status codes (200 for success, 404 for not found)

### 🛠️ Task 2: Implement CRUD Operations

#### Description

Complete the API by implementing all CRUD operations. Students will add endpoints to create new books, update existing ones, and delete books from the collection.

#### Requirements

Your API should:

- Implement a POST endpoint (`/books`) to create a new book with validation
- Implement a PUT endpoint (`/books/{book_id}`) to update an existing book
- Implement a DELETE endpoint (`/books/{book_id}`) to remove a book
- Include proper error handling (e.g., duplicate IDs, missing books)
- Return appropriate HTTP status codes (201 for created, 204 for deleted, 400 for bad requests)
- Store data in an in-memory list or dictionary (no database required)

### 🛠️ Task 3: Add Documentation and Testing

#### Description

Enhance your API with comprehensive documentation and create a simple test suite to verify all endpoints work correctly.

#### Requirements

Your submission should include:

- Docstrings for all endpoints with descriptions of request/response formats
- Use FastAPI's built-in interactive documentation (Swagger UI at `/docs` and ReDoc at `/redoc`)
- Create a `test_api.py` file with test cases for at least 5 different API scenarios
- Ensure all CRUD operations are tested and passing
- Include comments explaining the test logic

## 🚀 Getting Started

1. Download the starter code
2. Install dependencies: `pip install fastapi uvicorn`
3. Run the API: `uvicorn main:app --reload`
4. Visit `http://localhost:8000/docs` to explore the interactive API documentation

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc7231.html#status.codes)
- [REST API Best Practices](https://restfulapi.net/)
