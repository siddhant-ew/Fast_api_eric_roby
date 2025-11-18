from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI(title="This is Siddhant Kadiyal",summary="The CEO of NeuralNetVerse")


# class Book():
#     id : int
#     title : str
#     author : str
#     description : str
#     rating : int

#     def __init__(self, id, title, author, description, rating):
#         self.id = id
#         self.title = title 
#         self.author = author
#         self.description = description
#         self.rating = rating

class BookRequest(BaseModel):
    id : int
    title : str = Field(min_length=3)
    author : str = Field(min_length=3)
    description : str = Field(min_length=1, max_length=100)
    rating: int = Field(..., le=5)



BOOKS = [
    BookRequest(id=1, title='Computer Science Pro', author='codingwithcoby', description='A very nice book!', rating=5),
    BookRequest(id=2, title='Be Fast with FastAPI', author='codingwithroby', description='A great book!', rating=5),
    BookRequest(id=3, title='Master Endpoints', author='codingwithcoby', description='An awesome book!', rating=5),
    BookRequest(id=4, title='HP1', author='Author 1', description='Book Description', rating=2),
    BookRequest(id=5, title='HP2', author='Author 2', description='Book Description', rating=3),
    BookRequest(id=6, title='HP3', author='Author 3', description='Book Description', rating=1)
]


@app.get("/book-info")
async def book_info():
    return BOOKS

@app.post("/book-info/create-book")
async def create_book(create_book=Body()):
    BOOKS.append(create_book)
    return BOOKS


@app.post("/create-book")
async def create_book(create_book: BookRequest):
    print(type(BookRequest))
    BOOKS.append(create_book)
    return BOOKS

