
from src.library import Library, borrow_percentile


def test_borrow_percentile_with_no_loans():
    library = Library()

    result = borrow_percentile("member1", library)

    assert result == 0.0
