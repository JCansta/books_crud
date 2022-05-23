# Book CRUD In Fastapi

This project was designed to complete technical testing requirements.

## Installation

[uvicorn](https://www.uvicorn.org/) is required to start the project

```bash
$ pip install uvicorn
```

## Usage

```python
from fastapi import FastAPI, Header, HTTPException
from typing import Optional, Union
from pydantic import BaseModel

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

```
## Start de project
The main.py file contains the commands required to start the project
```bash
python3 main.py
```
But you can also start the project using the uvicorn command to the bookapi.py file directly
```bash
uvicorn v1/bookapi:app --reload
```
## Enter to the FASTAPI Docs
Once the project has started, you can access its documentation with the following link [Docs](http://127.0.0.1:8000/docs)

## Testing
A file has already been established in which all possible cases and their results are tested, giving all of them correct.

you have to install pytest first to be able to use the test file
```bash
$ pip install pytest
```
after install pytest, you can test the file using the following command on test_bookapi.py
```bash
$ pytest tests/test_bookapi.py
```