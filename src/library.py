from src.book import Book


def fine_tier(days_overdue: int) -> str:
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative.")
    elif days_overdue == 0:
        return "None"
    elif days_overdue <= 7:
        return "Low"
    elif days_overdue <= 14:
        return "Medium"
    elif days_overdue <= 30:
        return "High"
    else:
        return "Severe"


def validate_isbn(isbn: str) -> bool:
    if len(isbn) != 13:
        return False

    if not isbn.isdigit():
        return False

    return True


class Library:
    def __init__(self):
        self.books = {}
        self.member_loans = {}

    def add_book(self, book: Book) -> None:
        if book.book_id in self.books:
            raise ValueError("Duplicate ISBN is not allowed.")

        self.books[book.book_id] = book

    def borrow_book(self, member_id: str, isbn: str) -> None:
        current_loans = self.member_loans.get(member_id, 0)

        if current_loans >= 5:
            raise ValueError("Borrow limit exceeded.")

        if isbn not in self.books:
            raise ValueError("Book not found.")

        self.books[isbn].borrow_book()

        self.member_loans[member_id] = current_loans + 1


def borrow_percentile(member: str, library: Library) -> float:
    """Calculate a member's borrowing percentile."""
    loans = library.member_loans
    counts = list(loans.values())
    member_count = loans.get(member, 0)
    rank = counts.index(member_count)
    return rank / len(counts) * 100
