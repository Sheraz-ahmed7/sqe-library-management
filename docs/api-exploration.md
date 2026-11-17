
# LibraryHub API Exploration

## 1. Overview

This document records the manual exploration and testing of the LibraryHub REST API developed using Flask.

Base URL: `http://127.0.0.1:5000`

Testing environment:
- Python 3.11
- Flask
- PowerShell
- Invoke-RestMethod
- Local Flask development server

## 2. API Endpoints Tested

| HTTP Method | Endpoint | Description | Expected Status |
|---|---|---|---|
| POST | /members | Register a member | 201 |
| POST | /books | Add a new book | 201 |
| GET | /books | Retrieve all books | 200 |
| GET | /books/{isbn} | Retrieve a specific book | 200 |
| POST | /members/{id}/borrow | Borrow a book | 200 |
| POST | /members/{id}/return | Return a book | 200 |
| GET | /members/{id}/fines | Retrieve member fines | 200 |

## 3. Manual Test Data

Member:
- ID: 501

Book:
- Title: Clean Code
- ISBN: 9780132350884
- Author: R. Martin
- Total Copies: 2

## 4. Successful API Requests

### Test 1: Register Member

Method: POST

Endpoint: `/members`

Request body:

```json
{
  "id": 501
}
```

Expected status: 201 CREATED

Observed result: Member registered successfully.

### Test 2: Add Book

Method: POST

Endpoint: `/books`

Request body:

```json
{
  "title": "Clean Code",
  "isbn": "9780132350884",
  "author": "R. Martin",
  "total_copies": 2
}
```

Expected status: 201 CREATED

Observed result: Book added successfully with two available copies.

### Test 3: Retrieve All Books

Method: GET

Endpoint: `/books`

Expected status: 200 OK

Observed result: The API returned the list of available books.

### Test 4: Retrieve Book by ISBN

Method: GET

Endpoint: `/books/9780132350884`

Expected status: 200 OK

Observed result: The API returned the requested book details.

### Test 5: Borrow Book

Method: POST

Endpoint: `/members/501/borrow`

Request body:

```json
{
  "isbn": "9780132350884"
}
```

Expected status: 200 OK

Observed result: Book borrowed successfully. Available copies decreased from 2 to 1.

### Test 6: Return Book

Method: POST

Endpoint: `/members/501/return`

Request body:

```json
{
  "isbn": "9780132350884",
  "days_overdue": 4
}
```

Expected status: 200 OK

Observed result: Book returned successfully. Available copies increased to 2.

### Test 7: Retrieve Member Fines

Method: GET

Endpoint: `/members/501/fines`

Expected status: 200 OK

Observed result:
- Member ID: 501
- Days overdue: 4
- Fine tier: Low

## 5. Error Handling Tests

| Test Scenario | Expected Status | Observed API Response |
|---|---|---|
| Missing title | 400 | Missing required field: title |
| Invalid copies data type | 400 | total_copies must be a non-negative integer |
| Unknown ISBN | 404 | Book not found |

All three error responses matched the expected behavior.

## 6. Additional API Validation

The following cases were also tested using automated API tests:

- Borrowing a book with zero available copies returns 400.
- A member's sixth borrowing attempt returns 400.
- Borrowing with an unknown member returns 404.
- Borrowing an unknown book returns 404.
- Book response schema contains exactly four required fields:
  - title
  - isbn
  - author
  - available_copies

## 7. Automated Testing Results

The complete project test suite was executed using:

```powershell
py -3.11 -m pytest -v
```

Final result:

- Total tests: 58
- Passed: 58
- Failed: 0

All existing LibraryHub tests and new API tests passed successfully.

## 8. Conclusion

The LibraryHub REST API was manually explored and automatically tested.

The tested endpoints handled successful requests, invalid input, unavailable books, unknown resources, borrowing limits, and response schema validation as expected.

The API is running locally using Flask's development server and is suitable for local testing and further development.
