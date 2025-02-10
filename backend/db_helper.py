import mysql.connector
from contextlib import contextmanager


@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(

        host='localhost',
        user = 'root',
        password = 'root',
        database = 'expense_manager'
    )

    # if connection.is_connected():
    #     print('Connection successful')
    # else:
    #     print('Connection failed')

    cursor = connection.cursor(dictionary=True)

    yield cursor
    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("Select * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)



def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        # for expense in expenses:
        #     print(expense)
        return expenses

def insert_expense_for_date(expense_date, amount, category, notes):
    with get_db_cursor(commit = True) as cursor:
        cursor.execute(
            "INSERT INTO expenses(expense_date, amount, category, notes) VALUES (%s,%s,%s,%s)",
            (expense_date, amount, category, notes)
        )

def delete_expense_for_date(expense_date):
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute('''  
                        SELECT category, SUM(amount) as total
                        FROM expenses WHERE expense_date 
                        BETWEEN %s and %s 
                        GROUP BY category;
                       ''',
                       (start_date, end_date)
                    )
        data = cursor.fetchall()
        return data


if __name__ == '__main__':
    # fetch_all_records()
    
    # insert_expense_for_date("2024-08-20",300,"Food","Panipuri")
    # print("***expenses for 8/20 *****")
    expenses = fetch_expenses_for_date('2024-08-15')
    print(len(expenses))
    # print("***delete for 8/20 *****")
    # delete_expense_for_date('2024-08-20')

    # print("***again fetch expenses for 8/20 *****")
    # fetch_expenses_for_date('2024-08-20')
    # summary = (fetch_expense_summary("2024-08-01", "2024-08-05"))
    # for record in summary:
    #     print(record)


