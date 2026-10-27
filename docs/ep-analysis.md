# Lab 5 — Equivalence Partitioning Analysis

## 1. Objective

Use Equivalence Partitioning (EP) to select representative inputs
from valid and invalid classes and reduce redundant testing.

## 2. Input A: Days Overdue — fine_tier()

| Class | Input Domain | Representative | Expected Result |
|---|---|---|---|
| Invalid | Days < 0 | -3 | ValueError |
| Valid | Exactly 0 days | 0 | None |
| Valid | 1–7 days | 4 | Low |
| Valid | 8–14 days | 10 | Medium |
| Valid | 15–30 days | 20 | High |
| Valid | 31 or more days | 45 | Severe |

## 3. Input B: Number of Books on Loan

Business rule: A member may have between 0 and 5 books on loan.

| Class | Input Domain | Representative | Expected Result |
|---|---|---|---|
| Valid | 0–5 existing loans | 3 existing loans | A new loan is allowed |
| Invalid | 6 or more existing loans | 5 existing loans attempting a sixth loan | New loan is rejected |

Note: The representative for the invalid class describes the
member's current state and attempted action. The loan count becomes
six only if the system incorrectly accepts the new loan.

## 4. Input C: ISBN

Business rule: ISBN must contain exactly 13 numeric digits.

| Class | Input Domain | Representative | Expected Result |
|---|---|---|---|
| Valid | Exactly 13 numeric digits | "9781234567890" | Accepted |
| Invalid | Empty string | "" | Rejected |
| Invalid | Fewer than 13 characters | "12345" | Rejected |
| Invalid | Contains letters | "97812345678AB" | Rejected |
| Invalid | Contains symbols | "978-123456789" | Rejected |
| Invalid | More than 13 digits | "97812345678901" | Rejected |

## 5. Limitation of Equivalence Partitioning

EP reduces redundant tests by selecting representative values
from input classes. However, it can miss errors at class boundaries,
such as incorrectly accepting day 8 as Low instead of Medium.
Boundary Value Analysis (BVA) should be used alongside EP to
test values immediately below, at, and above important boundaries.

## 6. Test Execution Summary

The actual pytest summary will be added after executing the tests.