# added the validation for the query and path parameters 
# get the book by id, date, etc.
# added the published_date by the 

# 200 OK → Everything worked perfectly.
# 201 Created → Something new was created (like adding a new user).
# 204 No Content → Request was successful but there's nothing to show in the response.

# 400 Bad Request → The request is wrong or incomplete.
# 401 Unauthorized → You need to log in or provide a token.
# 403 Forbidden → You’re not allowed to access this.
# 404 Not Found → The thing you are looking for doesn’t exist.
# 409 Conflict → The request conflicts with existing data.

# 500 Internal Server Error → Something broke on the server.
# 502 Bad Gateway → Server received an invalid response from another server.
# 503 Service Unavailable → Server is down or too busy.
# 504 Gateway Timeout → Server took too long to respond.



from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

BOOKS = [
    {
        "id": 1,
        "title": "Title One",
        "author": "Author One",
        "category": "science",
        "description": "Description for Title One",
        "rating": 4,
        "published_date": 2010
    },
    {
        "id": 2,
        "title": "Title Two",
        "author": "Author Two",
        "category": "science",
        "description": "Description for Title Two",
        "rating": 5,
        "published_date": 2012
    },
    {
        "id": 3,
        "title": "Title Three",
        "author": "Author Three",
        "category": "history",
        "description": "Description for Title Three",
        "rating": 3,
        "published_date": 2008
    },
    {
        "id": 4,
        "title": "Title Four",
        "author": "Author One",
        "category": "math",
        "description": "Description for Title Four",
        "rating": 4,
        "published_date": 2015
    },
    {
        "id": 5,
        "title": "Title Five",
        "author": "Author Five",
        "category": "math",
        "description": "Description for Title Five",
        "rating": 5,
        "published_date": 2018
    }
]


class Book(BaseModel):
    id : int = Field(title="Book ID is needed")
    title : str = Field(min_length=3)
    author : str = Field(min_length=3)
    description : str = Field(min_length=3)
    rating : int = Field(gt=0,lt=30)
    published_date: int = Field(gt=1000,lt=2026)

    model_config ={
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title" : "A New Book",
                "author" : "Siddhant Kadiyal",
                "description": "A new description is added",
                "rating": 5,
                "published_date": 2010
            }
        }
    }
    
@app.get("/book-info")
async def book_info():
    return BOOKS

@app.post("/book-info/create-book")
async def create_book(create_book:Book):
    BOOKS.append(create_book.model_dump())
    return BOOKS

@app.get("/get-by-rating")
async def get_by_rating(book_rating: int = Query(gt=0,lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book['rating'] == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/update-book")
async def update_the_book(book: Book):
    for i in range(len(BOOKS)):
        if BOOKS[i]["id"] == book.id:      # compare ids
            BOOKS[i] = book.model_dump()   # replace old data
            return BOOKS[i]
    return {"error": "Book not found"}


@app.delete("/delete-book/{book_id}")
async def delete_the_book(book_id:int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i]["id"] == book_id:
            deleted_book = BOOKS.pop(i)
    return deleted_book

@app.get("/get-by-year")
async def get_by_date(year: int = Query(gt=1000,lt=2026)):
    books_to_show = []
    for j in BOOKS:
        if j["published_date"] == year:
            books_to_show.append(j)
    return books_to_show