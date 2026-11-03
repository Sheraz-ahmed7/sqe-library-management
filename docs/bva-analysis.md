# Boundary Value Analysis — Lab 6

## 1. Function: fine_tier()

**Specification:** The function classifies overdue days into fine tiers.

- Negative days: ValueError
- 0 days: None
- 1–7 days: Low
- 8–14 days: Medium
- 15–30 days: High
- 31 and above: Severe

### Boundary Analysis

| Boundary | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
|---:|---:|---|---:|---|---:|---|
| 0 (minimum) | -1 | ValueError | 0 | None | 1 | Low |
| 1 | 0 | None | 1 | Low | 2 | Low |
| 8 | 7 | Low | 8 | Medium | 9 | Medium |
| 15 | 14 | Medium | 15 | High | 16 | High |
| 31 | 30 | High | 31 | Severe | 32 | Severe |

### Selected Boundary Test Values

`-1, 0, 1, 7, 8, 9, 14, 15, 16, 30, 31, 32`

Total: 12 test cases.

### Purpose

Boundary Value Analysis checks whether `fine_tier()` correctly handles values immediately below, at, and above each boundary. It helps detect off-by-one errors.


---

## 2. Function: Library.borrow_book()

**Specification:** A member can borrow a maximum of 5 books.

- 0–4 books: Borrowing one more book is allowed.
- 5 books: Borrowing another book is rejected.
- More than 5 books: Borrowing is rejected.

### Boundary Analysis

| Current Loans | Attempt | Expected Result |
|---:|---|---|
| 4 | Borrow 1 book (total 5) | Success |
| 5 | Borrow 1 book (total 6) | ValueError |
| 6 | Borrow 1 book (total 7) | ValueError |

### Purpose

These tests verify that the borrowing limit is enforced correctly at its upper boundary and that members cannot borrow beyond the maximum limit.

---

## 3. Function: validate_isbn()

**Specification:** An ISBN must contain exactly 13 numeric digits.

### Boundary Analysis

| Boundary | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
|---:|---:|---|---:|---|---:|---|
| 13 digits | 12 | False | 13 | True | 14 | False |

### Additional Boundary Test

| ISBN Length | Expected Result |
|---:|---|
| 11 | False |
| 12 | False |
| 13 | True |
| 14 | False |
| 15 | False |

### Purpose

These tests verify that ISBN validation accepts exactly 13 digits and rejects strings that are shorter or longer than the required length.
