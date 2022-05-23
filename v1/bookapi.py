#!/usr/bin/env python3

from pydantic import BaseModel
from fastapi import FastAPI, Header, HTTPException, status
from typing import Union, Optional

app = FastAPI()

books = {
}

class Book(BaseModel):
    name: str
    pages: int
    author: str
    year: str

class UpdateBook(BaseModel):
    name: Optional[str] = None
    pages: Optional[int] = None
    author: Optional[str] = None
    year: Optional[str] = None

@app.get("/")
async def index():
    return books

@app.get("/get-book/{book_id}")
async def get_book(book_id: int = Header()):
    if book_id in books:
        return books[book_id]
    
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/create-book/{book_id}", status_code=status.HTTP_201_CREATED)
async def create_book(book_id: int = Header(), book: Union[Book, None] = None):
    if book_id in books:
        raise HTTPException(status_code=400, detail="Book Already Exists")

    books[book_id] = book
    return books[book_id]

@app.put("/update-book/{book_id}")
async def update_book(book_id: int = Header(), book : Union[UpdateBook, None] = None):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.name != None:
        books[book_id].name = book.name

    if book.pages != None:
        books[book_id].pages = book.pages

    if book.author != None:
        books[book_id].author = book.author
    
    if book.year != None:
        books[book_id].year = book.year

    return books[book_id]

@app.delete("/delete-book/{book_id}")
async def delete_book(book_id: int = Header()):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    
    del books[book_id]
    return {"Message": "book Deleted Succesfully"}