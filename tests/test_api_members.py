
def register_member(client, member_id="501"):
    return client.post(
        "/members",
        json={"id": member_id}
    )


def add_test_book(client):
    return client.post(
        "/books",
        json={
            "title": "Clean Code",
            "isbn": "9780132350884",
            "author": "R. Martin",
            "total_copies": 2
        }
    )


def test_register_member(client):
    response = register_member(client)

    assert response.status_code == 201
    assert response.json["id"] == "501"


def test_borrow_book(client):
    register_member(client)
    add_test_book(client)

    response = client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"}
    )

    assert response.status_code == 200
    assert response.json["available_copies"] == 1


def test_return_book(client):
    register_member(client)
    add_test_book(client)

    client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"}
    )

    response = client.post(
        "/members/501/return",
        json={
            "isbn": "9780132350884",
            "days_overdue": 4
        }
    )

    assert response.status_code == 200
    assert response.json["available_copies"] == 2
    assert response.json["days_overdue"] == 4


def test_get_member_fines(client):
    register_member(client)
    add_test_book(client)

    client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"}
    )

    client.post(
        "/members/501/return",
        json={
            "isbn": "9780132350884",
            "days_overdue": 4
        }
    )

    response = client.get("/members/501/fines")

    assert response.status_code == 200
    assert response.json["days_overdue"] == 4
    assert response.json["fine_tier"] == "Low"


def test_borrow_unknown_book(client):
    register_member(client)

    response = client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350999"}
    )

    assert response.status_code == 404
    assert response.json["error"] == "Book not found."


def test_borrow_unknown_member(client):
    response = client.post(
        "/members/999/borrow",
        json={"isbn": "9780132350884"}
    )

    assert response.status_code == 404
    assert response.json["error"] == "Member not found."
