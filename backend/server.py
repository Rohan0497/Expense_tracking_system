# from fastapi import FastAPI, Body
# from datetime import date
# import db_helper
# from typing import List
# from pydantic import BaseModel

# class Expense(BaseModel):
#     # expense_date : date
#     amount : float
#     category: str
#     notes : str

# app = FastAPI()

# @app.get("/expenses/{expense_date}",response_model = List[Expense])
# def get_expense(expense_date : date):
   
#     expenses = db_helper.fetch_expenses_for_date(expense_date)
#     return expenses

# @app.post("/expenses/{expense_date}")
# def add_or_update_expense(expense_date: date, expenses : List[Expense]):
#     db_helper.delete_expense_for_date(expense_date)
#     for expense in expenses:
#         db_helper.insert_expense_for_date(expense_date, expense.amount, expense.category, expense.notes)

#     return {'message' : "Successfully build expense"}



from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")

    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully"}