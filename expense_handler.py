from splitwise.expense import Expense
from splitwise.user import ExpenseUser


def create_expense_user(user_id, paid_share, owed_share):
    u = ExpenseUser()
    u.setId(user_id)
    u.setPaidShare(str(paid_share))
    u.setOwedShare(str(owed_share))
    return u


def create_expense(group_id, total_amount, description, users, details=""):
    expense = Expense()
    expense.setGroupId(group_id)
    expense.setCost(str(total_amount))
    expense.setDescription(description)
    expense.setCurrencyCode("USD")
    expense.setUsers(users)
    expense.setDetails(details)
    return expense


def submit_expense(sObj, group, users, total_amount, title, details=""):
    expense = create_expense(group.getId(), total_amount, title, users, details)
    new_expense, errors = sObj.createExpense(expense)

    if errors:
        print(f"[ERROR] Expense not added: {errors}")
    else:
        print(f"[SUCCESS] Expense added. ID: {new_expense.getId()}")
