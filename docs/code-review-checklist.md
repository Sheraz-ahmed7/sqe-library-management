# Code Review Checklist — SQE Lab 9

## 1. Correctness
- [ ] The function produces the expected result for valid inputs.
- [ ] Boundary conditions and edge cases are handled.
- [ ] Invalid or unexpected inputs are handled appropriately.

## 2. Tests
- [ ] Tests cover normal and boundary cases.
- [ ] Tests cover empty collections and missing members.
- [ ] Tests verify expected behavior.

## 3. Readability
- [ ] Function and variable names are meaningful.
- [ ] Code formatting is consistent and easy to read.
- [ ] Functions have useful docstrings where appropriate.

## 4. Design
- [ ] The code follows existing project structure and conventions.
- [ ] Unnecessary duplication is avoided.
- [ ] Each function has a clear responsibility.

## 5. Risk
- [ ] Input validation handles unexpected inputs safely.
- [ ] The change does not introduce unnecessary performance problems.
- [ ] Existing functionality remains compatible.

## Retrospective
- Most valuable checklist item: Checking boundary conditions helps identify errors in percentile calculations and small collections.
- Checklist improvement for next time: Add an explicit requirement to run automated tests before approving a pull request.