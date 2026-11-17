
def register_member(client):
    return client.post(
        "/members",
        json={"id": "501"}
    )


def add_book(client, copies=1):
    return client.post(
        "/books",
        json={
            "title": "Test Book",
            "isbn": "9780132350884",
            "author": "Test Author",
            "total_copies": copies
        }
    )


def test_borrow_book_with_zero_copies(client):
    register_member(client)
    add_book(client, copies=0)

    response = client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"}
    )

    assert response.status_code == 400
    assert response.json["error"] == "No copies available to borrow."


def test_sixth_borrow_attempt(client):
    register_member(client)
    add_book(client, copies=6)

    # First five borrowing attempts should succeed.
    for _ in range(5):
        response = client.post(
            "/members/501/borrow",
            json={"isbn": "9780132350884"}
        )
        assert response.status_code == 200

    # Sixth borrowing attempt should fail.
    response = client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Borrow limit exceeded."
