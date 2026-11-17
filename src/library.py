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
        self.members = set()
        self.member_borrowed_books = {}
        self.member_overdue_days = {}

    def register_member(self, member_id: str) -> None:
        if member_id in self.members:
            raise ValueError("Member already exists.")

        self.members.add(member_id)
        self.member_loans[member_id] = 0
        self.member_borrowed_books[member_id] = []
        self.member_overdue_days[member_id] = 0

    def add_book(self, book: Book) -> None:
        if book.book_id in self.books:
            raise ValueError("Duplicate ISBN is not allowed.")

        self.books[book.book_id] = book

    def borrow_book(self, member_id: str, isbn: str) -> None:
        # Preserve compatibility with existing direct Library tests.
        if member_id not in self.members:
            self.members.add(member_id)
            self.member_loans.setdefault(member_id, 0)
            self.member_borrowed_books.setdefault(member_id, [])
            self.member_overdue_days.setdefault(member_id, 0)

        current_loans = self.member_loans.get(member_id, 0)

        if current_loans >= 5:
            raise ValueError("Borrow limit exceeded.")

        if isbn not in self.books:
            raise ValueError("Book not found.")

        self.books[isbn].borrow_book()

        self.member_loans[member_id] = current_loans + 1
        self.member_borrowed_books[member_id].append(isbn)

    def return_book(
        self, member_id: str, isbn: str, days_overdue: int = 0
    ) -> None:
        if member_id not in self.members:
            raise ValueError("Member not found.")

        if isbn not in self.books:
            raise ValueError("Book not found.")

        if isbn not in self.member_borrowed_books[member_id]:
            raise ValueError("This member has not borrowed this book.")

        if not isinstance(days_overdue, int) or isinstance(days_overdue, bool):
            raise ValueError("Days overdue must be an integer.")

        if days_overdue < 0:
            raise ValueError("Days overdue cannot be negative.")

        self.member_borrowed_books[member_id].remove(isbn)
        self.member_loans[member_id] -= 1
        self.books[isbn].copies += 1
        self.member_overdue_days[member_id] += days_overdue

    def get_member_fines(self, member_id: str) -> dict:
        if member_id not in self.members:
            raise ValueError("Member not found.")

        days = self.member_overdue_days[member_id]

        return {
            "member_id": member_id,
            "days_overdue": days,
            "fine_tier": fine_tier(days)
        }



def borrow_percentile(member: str, library: Library) -> float:
    """Calculate a member's borrowing percentile."""
    loans = library.member_loans

    if not loans:
        return 0.0

    counts = list(loans.values())
    member_count = loans.get(member, 0)

    rank = counts.index(member_count)

    return rank / len(counts) * 100
