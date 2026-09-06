import pytest
from src.book import Book


def test_borrow_book_when_no_copies_available():
    book = Book(
        "Python Programming",
        "John Smith",
        "9781234567890",
        0
    )

    with pytest.raises(ValueError, match="No copies available to borrow"):
        book.borrow_book()

    assert book.copies == 0