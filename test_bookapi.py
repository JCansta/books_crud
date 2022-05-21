#!/usr/bin/env python3

from fastapi.testclient import TestClient
from .bookapi import app

client = TestClient(app)

def test_create_bookapi():
    response = client.post(
        '/create-book/1',
        json={"name": "Hola", "pages": 20, "author": "Mundo", "year": "2022"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Hola",
        "pages": 20,
        "author": "Mundo",
        "year": "2022"
    }

def test_create_id_already_exist_bookapi():
    response = client.post(
        '/create-book/1',
        json={"name": "Hola", "pages": 20, "author": "Mundo", "year": "2022"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Book Already Exists"}


def test_get_bookapi():
    response = client.get('/get-book/1')
    assert response.status_code == 200
    assert response.json() == {
        "name": "Hola",
        "pages": 20,
        "author": "Mundo",
        "year": "2022"
    }

def test_bad_get_bookapi():
    response = client.get('/get-book/2')
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_update_bookapi():
    response = client.put(
        '/update-book/1',
        json={"name": "looking", "pages": 40, "author": "for", "year": "errors"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "looking",
        "pages": 40,
        "author": "for",
        "year": "errors"
    }

def test_update_incomplete_bookapi():
    response = client.put(
        '/update-book/1',
        json={"name": "updating", "pages": 20, "year": "incomplete"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "updating",
        "pages": 20,
        "author": "for",
        "year": "incomplete"
    }

def test_update_id_not_exist_bookapi():
    response = client.put(
        '/update-book/3',
        json={"name": "looking", "pages": 40, "author": "for", "year": "errors"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_delete_bookapi():
    response = client.delete('/delete-book/1')
    assert response.status_code == 200
    assert response.json() == {"Message": "book Deleted Succesfully"}

def test_delete_bad_id_bookapi():
    response = client.delete('/delete-book/1')
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}