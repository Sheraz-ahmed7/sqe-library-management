# Requirements Traceability Matrix (RTM)

| Requirement ID | Requirement Description | Test Case IDs | Coverage |
|---|---|---|---|
| REQ-1 | Add a book with a valid ISBN | TC-001 | Covered |
| REQ-2 | Reject duplicate ISBNs | TC-002 | Covered |
| REQ-3 | Reject malformed ISBNs | TC-003 | Covered |
| REQ-4 | Borrow books when copies are available | TC-004 | Covered |
| REQ-5 | Reject borrowing when no copies are available | TC-005 | Covered |
| REQ-6 | Support valid returns and reject invalid returns | TC-006, TC-007 | Covered |
| REQ-7 | Enforce a maximum of five active loans | TC-008, TC-009 | Covered |
| REQ-8 | Calculate fine tiers correctly | TC-010, TC-011, TC-012 | Covered |

## Coverage Review
All eight listed requirements have at least one planned test case.

Coverage means that a test has been mapped to a requirement.
It does not mean that the test has passed.

Any requirement that cannot be tested because the feature is missing
must be reported and tracked until it is resolved.