import os
import sqlite3
import pytest
from main2 import init_db, add_expense, add_income, get_expenses, get_income, delete_entry

TEST_DB = "test_budget.db"

@pytest.fixture(autouse=True)
def setup_db(monkeypatch):
    """
    Creates a fresh test database before each test
    and deletes it after the test finishes.
    """

    monkeypatch.setenv("DB_NAME", TEST_DB)

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    init_db()

    yield

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_add_expense(setup_db):
    add_expense("Coffee", 5.0, "Food")

    expenses = get_expenses()

    assert len(expenses) == 1
    assert expenses[0][1] == "Coffee"
    assert expenses[0][2] == 5.0
    assert expenses[0][3] == "Food"


def test_add_income(setup_db):
    add_income("Salary", 1200.0, "Job")

    income = get_income()

    assert len(income) == 1
    assert income[0][1] == "Salary"
    assert income[0][2] == 1200.0
    assert income[0][3] == "Job"


def test_get_multiple_entries(setup_db):
    add_expense("Coffee", 5.0, "Food")
    add_expense("Bus", 3.0, "Transport")
    add_income("Gift", 100.0, "Other")

    expenses = get_expenses()
    income = get_income()

    assert len(expenses) == 2
    assert len(income) == 1



def test_delete_expense(setup_db):
    add_expense("Snack", 3.5, "Food")

    expenses = get_expenses()
    entry_id = expenses[0][0]

    delete_entry("expenses", entry_id)

    expenses_after = get_expenses()
    assert len(expenses_after) == 0


def test_delete_income(setup_db):
    add_income("Bonus", 200.0, "Job")

    income = get_income()
    entry_id = income[0][0]

    delete_entry("income", entry_id)

    income_after = get_income()
    assert len(income_after) == 0


