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