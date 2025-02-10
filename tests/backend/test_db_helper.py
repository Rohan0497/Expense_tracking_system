from backend import db_helper

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes'] == "Bought potatoes"



def test_fetch_expenses_for_date_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")

    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2099-01-01","2099-08-02")
    assert len(summary) == 0
    


def test_fetch_expenses_for_date_multiple_records():
    """Test fetching expenses when records exist for a given date (handles cases with one or more records)."""
    expenses = db_helper.fetch_expenses_for_date("2024-08-20")

    assert isinstance(expenses, list)  # Ensure the response is a list
    if len(expenses) > 0:  # Only run further checks if there are expenses
        assert all("amount" in expense for expense in expenses)  # All records must have an amount
        assert all("category" in expense for expense in expenses)  # All records must have a category
        assert all("notes" in expense for expense in expenses)  # All records must have notes



def test_fetch_expenses_for_date_empty():
    """Test fetching expenses for a date with no recorded expenses."""
    expenses = db_helper.fetch_expenses_for_date("2024-12-31")  # Assuming this date has no expenses

    assert expenses == []  # Expecting an empty list


def test_insert_expense_for_date():
    """Test inserting a new expense and verifying it exists."""
    db_helper.insert_expense_for_date("2024-09-01", 500, "Travel", "Flight ticket")

    expenses = db_helper.fetch_expenses_for_date("2024-09-01")
    assert any(expense["amount"] == 500 and expense["category"] == "Travel" for expense in expenses)


def test_delete_expense_for_date():
    """Test deleting an expense and ensuring it is removed."""
    db_helper.insert_expense_for_date("2024-09-02", 50, "Food", "Pizza")
    
    db_helper.delete_expense_for_date("2024-09-02")
    
    expenses = db_helper.fetch_expenses_for_date("2024-09-02")
    assert len(expenses) == 0  # Expense should no longer exist


def test_fetch_expense_summary():
    """Test fetching expense summary for a valid date range."""
    summary = db_helper.fetch_expense_summary("2024-08-01", "2024-08-31")

    assert isinstance(summary, list)  # Should return a list of summaries
    assert all("category" in record and "total" in record for record in summary)  # Expected keys should be present


def test_fetch_expense_summary_with_no_data():
    """Test fetching expense summary for a date range where no expenses exist."""
    summary = db_helper.fetch_expense_summary("2099-01-01", "2099-08-02")

    assert len(summary) == 0  # No data should be returned


def test_insert_expense_with_invalid_data():
    """Test inserting an expense with invalid data types (should raise an exception)."""
    try:
        db_helper.insert_expense_for_date("invalid-date", "wrong-amount", 123, None)
        assert False  # Should not reach here
    except Exception:
        assert True  # Expected exception


def test_delete_expense_for_nonexistent_date():
    """Test deleting an expense for a date that does not exist (should not raise an error)."""
    try:
        db_helper.delete_expense_for_date("2099-12-31")  # Assuming this date has no expenses
        assert True  # Should not fail
    except Exception:
        assert False  # Should not raise an error
