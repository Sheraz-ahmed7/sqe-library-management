import pytest
from src.book import Book
from src.library import Library


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


def test_duplicate_isbn_is_rejected():
    library = Library()

    book1 = Book(
        "Python Programming",
        "John Smith",
        "9781234567890",
        2
    )

    book2 = Book(
        "Advanced Python",
        "Jane Smith",
        "9781234567890",
        3
    )

    library.add_book(book1)

    with pytest.raises(ValueError, match="Duplicate ISBN is not allowed"):
        library.add_book(book2)