# LibraryHub Software Test Plan

## 1. Introduction

This Test Plan defines the testing strategy for the LibraryHub module.
The purpose is to verify that book management, borrowing, member-related
operations, searching, and fine-related functionality behave according to
their requirements. Testing will include functional, negative/error-path,
non-functional, and regression testing.

## 2. Test Items

The following LibraryHub components are included in testing:

- Book creation and validation
- ISBN validation and duplicate ISBN detection
- Book borrowing and copy management
- Book return operations
- Member borrowing limits
- Fine calculation
- Book search functionality
- Regression tests for previously identified defects

## 3. Features to be Tested

The following features will be tested:

- Adding books with valid and invalid ISBN values
- Preventing duplicate ISBN values
- Borrowing books when copies are available
- Rejecting borrowing when no copies are available
- Returning borrowed books
- Rejecting invalid return operations
- Enforcing member borrowing limits
- Calculating fines for overdue books
- Searching for books
- Regression testing of defects fixed in Lab 3

## 4. Features Not to be Tested

The graphical user interface is out of scope for this test plan because the
current LibraryHub implementation is primarily a Python codebase rather than
a complete GUI application. Database performance, network infrastructure,
deployment infrastructure, and third-party services are also outside the
scope of this lab. Testing will focus on the available LibraryHub logic and
its documented requirements.

## 5. Test Approach

Testing will combine positive, negative, functional, non-functional, and
regression testing. Positive tests verify that valid operations produce the
expected results, while negative tests verify that invalid operations are
properly rejected. Regression tests will confirm that defects fixed during
Lab 3 remain fixed. Tests will be executed manually using the Python
environment and Python shell where functionality is available.

## 6. Pass/Fail Criteria

Testing will be considered successful when at least 95% of executable planned
test cases pass and zero Critical defects remain open. A test case will pass
when the actual result matches the expected result. A test case will fail when
the software produces an incorrect result or does not enforce a required
validation rule. Tests for functionality that is not implemented will be
marked Blocked rather than incorrectly marked as Passed.

## 7. Test Deliverables

The following testing deliverables will be produced:

- Software Test Plan
- Test Case document containing 12 test cases
- Requirements Traceability Matrix
- Manual test execution results
- Regression test results
- GitHub defect issues for any confirmed failures

## 8. Environmental Needs

Testing requires a Windows development environment with Python 3.11,
Git, GitHub access, VS Code, and the LibraryHub repository. The Python
environment will be used to execute the available LibraryHub functions and
regression tests. GitHub will be used for issue tracking, documentation
storage, and defect reporting.

## 9. Schedule

Testing activities will be completed during the Lab 4 session. The first
part of the session will be used to create the Test Plan, followed by test
case design and the Requirements Traceability Matrix. The final part of the
session will be used to manually execute the test cases and record the
results.

## 10. Risks

Some LibraryHub features required by the test cases may not yet be
implemented in the current codebase. Such tests will be marked Blocked and
will not be counted as successful executions. Changes to the code during
testing may also introduce regression defects. Incorrect test data or
incomplete requirements may lead to inaccurate test results.

## 11. Test Completion Criteria

Testing for the current lab will be considered complete when all 12 planned
test cases have documented execution results, all executable tests have been
evaluated, all requirements are traced to at least one test case, and any
confirmed failures have corresponding GitHub issues.
