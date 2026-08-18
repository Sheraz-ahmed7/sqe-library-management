class Book:
    def __init__(self, title: str, author: str, isbn: str, copies: int):
        if copies < 0:
            raise ValueError("Copies cannot be negative.")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def borrow_book(self) -> None:
        if self.copies <= 0:
            raise ValueError("No copies available to borrow.")
        self.copies -= 1