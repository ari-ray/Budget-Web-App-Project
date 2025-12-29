# Budget Web App - TESTS

This folder contains the **tests** for the Budget Web App.
The tests are designed to verify the correctness, validation and basic functionality of the application.

---

## Purpose
- Ensure that core functionality works as expected
- Validate input handling and server-side validation
- Detect regressions during future refactors or deployments

---

## Test Coverage
Currently the test focusees on:
- Database Setup
  - Initializes a fresh test database for each test
  - Ensures tests are isolated and do not affect real data
- Adding entries
  - test_add_expense: Adds an expense and verifies its details
  - test_add_income: Adds an income entry and verifies its details
- Retrieving multiple entries
  - test_get_multiple_entries: Ensures multiple income and expense entries are returned correctly
- Deleting entries
  - test_delete_expense: Deletes an expense and ensures it is removed
  - test_delete_income: Deletes an income entry and ensures it is removed

---

## How it Works
- The tests use a temporary database (test_budget.db) set via an environment variable.
- Each test runs with a fresh database and cleans up after itself.
- Pytest fixtures (setup_db) handle setup and teardown automatically.

---

## How to Run
- Make sure you are in the root directory of the project
- Install dependencies:
```bash
pip install pytest
```

- Run the tests from the root or the tests folder:
```bash
pytest
```
  - All tests will automatically initialise and clean up the temporary database
  - A summary will be shown indicating passed/failed tests

---

## Notes
- These tests focus on backend functionality and do not cover the frontend interface.
- Designed for learning and basic verification and hence they are not full production-grade unit tests.
- For more advanced testing,the following tests can be added:
  - Form validation errors
  - CSV export
  - Integration with the Flask routes









