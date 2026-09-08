# LibraryHub Test Cases

## Test Case Summary

This document contains the functional, negative, and regression test cases
for the LibraryHub module. Each test case is traceable to one or more
functional requirements.

| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type |
|---|---|---|---|---|---|---|---|
| TC-001 | Add book with valid new ISBN | REQ-1 | Library is available and ISBN `9780132350884` does not already exist | 1. Create a Book with title `Clean Code`, author `Robert Martin`, ISBN `9780132350884`, and 2 copies. 2. Add the book to the library. | Book is added successfully and the library contains the new ISBN. | High | Positive / Functional |
| TC-002 | Reject duplicate ISBN on add_book | REQ-2 | Library already contains a book with ISBN `9780132350884` | 1. Create another Book using ISBN `9780132350884`. 2. Call `library.add_book()` with the second book. | A `ValueError` is raised and the library still contains only one book with that ISBN. | High | Negative / Functional |
| TC-003 | Reject malformed ISBN | REQ-3 | Library is available | 1. Create a Book using malformed ISBN `ABC-123`. 2. Attempt to add the book to the library. | The system rejects the malformed ISBN and raises an appropriate validation error. | High | Negative / Functional |
| TC-004 | Borrow book when copies are available | REQ-4 | A book exists with at least 1 available copy | 1. Create a book with 2 copies. 2. Call `borrow_book()`. | Borrowing succeeds and the available copy count decreases from 2 to 1. | High | Positive / Functional |
| TC-005 | Reject borrowing when no copies are available | REQ-4 | A book exists with 0 available copies | 1. Create a book with 0 copies. 2. Call `borrow_book()`. | A `ValueError` is raised and the available copy count remains 0. | Critical | Negative / Regression |
| TC-006 | Return a book currently on loan | REQ-5 | Member has borrowed the specified book | 1. Borrow the book using the member. 2. Return the same book using `return_book()`. | The return succeeds and the book becomes available again. | High | Positive / Functional |
| TC-007 | Reject return of book not on loan by member | REQ-5 | Member has not borrowed the specified book | 1. Attempt to return a book that the member did not borrow. | The system rejects the return and raises an appropriate error without changing the member's loan records. | High | Negative / Functional |
| TC-008 | Member borrows at allowed limit | REQ-6 | Member is one book below the maximum borrowing limit and all books are available | 1. Borrow books until the member reaches the allowed limit. 2. Borrow the final permitted book. | The final permitted borrowing succeeds and the member reaches the maximum allowed number of loans. | High | Positive / Functional |
| TC-009 | Reject member borrowing beyond allowed limit | REQ-6 | Member has already reached the maximum borrowing limit | 1. Attempt to borrow one additional book. | The system rejects the additional borrowing and reports that the borrowing limit has been reached. | High | Negative / Functional |
| TC-010 | Fine calculation for zero days overdue | REQ-7 | Fine calculation is available and the book is returned on time | 1. Calculate the fine for 0 overdue days. | The calculated fine is `0`. | Medium | Positive / Functional |
| TC-011 | Fine calculation for mid-range overdue period | REQ-7 | Fine calculation is available | 1. Calculate the fine for 5 overdue days. | The system calculates the fine according to the defined LibraryHub fine rate for 5 overdue days. | Medium | Positive / Functional |
| TC-012 | Fine calculation at overdue-tier boundary | REQ-7 | Fine calculation uses defined overdue tiers | 1. Calculate the fine at the first overdue-tier boundary, such as 7 overdue days. | The system applies the correct fine rate for the boundary value and does not incorrectly use the previous tier. | High | Boundary / Functional |
