from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author One', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'}
]


class Book(BaseModel):
    id : int = Field(title="Book ID is needed")
    title : str = Field(min_length=3)
    author : str = Field(min_length=3)
    description : str = Field(min_length=3)
    rating : int = Field(gt=0,lt=30)

    model_config ={
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title" : "A New Book",
                "author" : "Siddhant Kadiyal",
                "description": "A new description is added",
                "rating": 5
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

