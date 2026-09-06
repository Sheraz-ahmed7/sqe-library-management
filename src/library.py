from src.book import Book


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book) -> None:
        if book.book_id in self.books:
            raise ValueError("Duplicate ISBN is not allowed.")

        self.books[book.book_id] = book