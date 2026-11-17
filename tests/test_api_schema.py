
def test_books_response_schema(client):
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

    book = response.json[0]

    expected_keys = {
        "title",
        "isbn",
        "author",
        "available_copies"
    }

    assert set(book.keys()) == expected_keys

    assert isinstance(book["title"], str)
    assert isinstance(book["isbn"], str)
    assert isinstance(book["author"], str)
    assert isinstance(book["available_copies"], int)
