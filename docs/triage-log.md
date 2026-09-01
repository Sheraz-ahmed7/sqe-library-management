# Defect Triage Log

## v0.2 — Library Management

| Rank | Issue | Severity | Priority | Decision |
|---|---|---|---|---|
| 1 | #5 — Borrowing a Book With No Available Copies | Critical | P0 | Fix |
| 2 | #7 — Duplicate ISBN values are allowed for different books | High | P1 | Fix |
| 3 | #6 — Negative number of book copies can be entered | High | P1 | Fix |
| 4 | #9 — Returning a book can increase available copies beyond original inventory | Medium | P2 | Won't fix this sprint |
| 5 | #8 — Book search is case-sensitive | Medium | P2 | Won't fix this sprint |

## Prioritization Rationale

Issue #5 is ranked first because allowing a book to be borrowed when no copies are available can compromise the core borrowing workflow and library inventory integrity.

Issue #7 is ranked second because duplicate ISBN values can make book identification ambiguous and may affect searching, borrowing, and inventory management.

Issue #6 is ranked third because negative copy values create invalid inventory data. Although serious, it has a lower impact than allowing unavailable books to be borrowed.

Issue #9 is ranked fourth because incorrect return handling can affect inventory accuracy, but it is less urgent than the P0 and P1 defects.

Issue #8 is ranked fifth because case-sensitive searching mainly affects usability and users can work around the problem by entering the exact capitalization.

## Severity vs Priority Trade-offs

Issue #6 has High severity and P1 priority because invalid book-copy values can corrupt inventory data and should be prevented.

Issue #8 has Medium severity and P2 priority because the system remains functional and users can work around the search problem.

Issue #9 has Medium severity and P2 priority because it affects inventory accuracy but does not completely prevent the main library functions from operating.

## Sprint Decision

This sprint will fix the three highest-priority defects:

1. Prevent borrowing when no copies are available.
2. Prevent duplicate ISBN values.
3. Prevent negative book-copy values.

The case-sensitive search defect and duplicate-return inventory defect will be deferred to a future sprint.