BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author One', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'}
]


from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel

## Data validation model
class Book(BaseModel):
    title : str
    author : str
    category : str

app = FastAPI(title="This is Siddhant Kadiyal",summary="The CEO of NeuralNetVerse")
print("app is started")

## GET method

@app.get("/health-checkup")
async def health_checkup():
    return "All database and connections are perfectly working!"

@app.get("/book-info")
async def read_all_books():
    return 

@app.get("/book-info/author-book")
async def author_book(author: str):
    specific_author = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            specific_author.append(book)
    return specific_author


@app.get("/book-info/specific-book")
async def specific_book_details(book_title:str):
    for book in BOOKS:
        if book_title.casefold() == book.get('title').casefold():
            return book
        
## DELETE method

@app.delete("/book-info/{book_title}")
async def delete_book(book_title:str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            BOOKS.remove(book)
    return BOOKS

## GET method

@app.get("/book-info/{title}")
async def dynamic_param(title:str, category:str):
    book_to_return = []
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold() and book.get('category').casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return

@app.get("/book-info/")
async def get_category (category:str):
    book_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return

## POST method

@app.post("/book-info/create_book")
async def create_book(new_book:Book):
    BOOKS.append(new_book)
    return BOOKS


## PUT method

@app.put("/book-info/update-book")
async def update_book(update_book: Book):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.title.casefold():
            BOOKS[i] = update_book.model_dump()
    return BOOKS


# Assignment

# Here is your opportunity to keep learning!
# 1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.

# @app.get("/book-info/author-book")
# async def author_book(author:str):
#     specific_author = []
#     for book in BOOKS:
#         if book.get('author').casefold() == author.casefold():
#             specific_author.append(book)
#     return specific_author

# Path Parameters:
# These are part of the URL path itself.
# You define them in the route path using curly braces {}.
# They are used when you want to identify a specific resource.

# Query Parameters:
# These are optional key-value pairs that come after the “?” in the URL.
# They are typically used to filter or modify the request.

# Summary Table

# | Type  | Location                         | Example URL | Example Parameter   | Common Use                 |
# | ----- | -------------------------------- | ----------- | ------------------- | -------------------------- |
# | Path  | `/users/{user_id}`               | `/users/10` | `user_id = 10`      | Identify specific resource |
# | Query | `/items/?category=books&limit=5` | after `?`   | `category`, `limit` | Filter, search, pagination |


