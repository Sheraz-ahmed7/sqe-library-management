import pytest

from src.library import validate_isbn


@pytest.mark.parametrize('isbn', [
    '9781234567890',
])
def test_valid_isbn(isbn):
    assert validate_isbn(isbn) is True


@pytest.mark.parametrize('isbn', [
    '',
    '123456789',
    '978123ABC7890',
    '97812345678-90',
    '97812345678901',
])
def test_invalid_isbn(isbn):
    assert validate_isbn(isbn) is False


@pytest.mark.parametrize("length, expected", [
    (11, False),
    (12, False),
    (13, True),
    (14, False),
    (15, False),
])
def test_isbn_length_boundaries(length, expected):
    isbn = "1" * length

    assert validate_isbn(isbn) is expected
