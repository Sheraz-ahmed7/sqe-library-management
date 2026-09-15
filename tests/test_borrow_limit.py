import pytest

from src.book import Book
from src.library import Library


def create_library():
    library = Library()
    library.add_book(Book("Book 1", "Author 1", "ISBN001", 10))
    return library


def borrow_books(library, member_id, count):
    for _ in range(count):
        library.borrow_book(member_id, "ISBN001")


@pytest.mark.parametrize('loan_count', [0, 3, 4])
def test_valid_borrow_limit(loan_count):
    library = create_library()

    borrow_books(library, "member1", loan_count)

    assert library.member_loans.get("member1", 0) == loan_count


@pytest.mark.parametrize('loan_count', [5])
def test_fifth_book_is_allowed(loan_count):
    library = create_library()

    borrow_books(library, "member1", loan_count)

    assert library.member_loans["member1"] == 5


def test_member_with_three_books_cannot_borrow_sixth():
    library = create_library()

    borrow_books(library, "member1", 3)

    with pytest.raises(ValueError):
        for _ in range(3):
            library.borrow_book("member1", "ISBN001")


def test_member_with_five_books_cannot_borrow_sixth():
    library = create_library()

    borrow_books(library, "member1", 5)

    with pytest.raises(ValueError):
        library.borrow_book("member1", "ISBN001")