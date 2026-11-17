
def test_add_book(client):
    response = client.post(
        "/books",
        json={
            "title": "Clean Code",
            "isbn": "9780132350884",
            "author": "R. Martin",
            "total_copies": 2
        }
    )

    assert response.status_code == 201
    assert response.json["title"] == "Clean Code"
    assert response.json["isbn"] == "9780132350884"
    assert response.json["available_copies"] == 2


def test_get_all_books(client):
    client.post(
        "/books",
        json={
            "title": "Clean Code",
            "isbn": "9780132350884",
            "author": "R. Martin",
            "total_copies": 2
        }
    )

    response = client.get("/books")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["title"] == "Clean Code"


def test_get_book_by_isbn(client):
    client.post(
        "/books",
        json={
            "title": "Clean Code",
            "isbn": "9780132350884",
            "author": "R. Martin",
            "total_copies": 2
        }
    )

    response = client.get("/books/9780132350884")

    assert response.status_code == 200
    assert response.json["isbn"] == "9780132350884"


def test_get_unknown_book(client):
    response = client.get("/books/9780132350999")

    assert response.status_code == 404
    assert response.json["error"] == "Book not found."


def test_add_book_missing_title(client):
    response = client.post(
        "/books",
        json={
            "isbn": "9780132350885",
            "author": "Test Author",
            "total_copies": 2
        }
    )

    assert response.status_code == 400
    assert response.json["error"] == "Missing required field: title"


def test_add_book_invalid_copies(client):
    response = client.post(
        "/books",
        json={
            "title": "Test Book",
            "isbn": "9780132350885",
            "author": "Test Author",
            "total_copies": "two"
        }
    )

    assert response.status_code == 400
    assert response.json["error"] == (
        "total_copies must be a non-negative integer."
    )
