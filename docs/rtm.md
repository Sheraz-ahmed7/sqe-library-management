# LibraryHub Requirements Traceability Matrix

| Requirement ID | Requirement | Test Case IDs | Coverage Status |
|---|---|---|---|
| REQ-1 | The system shall allow adding a book with a valid new ISBN. | TC-001 | Covered |
| REQ-2 | The system shall reject duplicate ISBN values. | TC-002 | Covered |
| REQ-3 | The system shall reject malformed ISBN values. | TC-003 | Covered |
| REQ-4 | The system shall allow borrowing when copies are available and reject borrowing when none are available. | TC-004, TC-005 | Covered |
| REQ-5 | The system shall correctly process book returns and reject invalid returns. | TC-006, TC-007 | Covered |
| REQ-6 | The system shall enforce the member borrowing limit. | TC-008, TC-009 | Covered |
| REQ-7 | The system shall calculate fines correctly based on overdue days. | TC-010, TC-011, TC-012 | Covered |
| REQ-8 | The system shall support book search functionality. | TC-013 | Covered |


## Traceability Summary

All eight LibraryHub requirements are now linked to at least one test case.
No requirement remains untraced. The addition of TC-013 closes the coverage
gap identified for the book search requirement.