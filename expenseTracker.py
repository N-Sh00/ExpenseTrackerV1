from expense import Expense
import calendar
import datetime

def main():
    print(f"Running the expense tracker")
    expense_file_path = "expenses.csv"
    budget = float(input("How much is your monthly budget?\n"))

    #Get user input for expense
    expense = get_user_expense()
    print(expense)

    #Write expense to a file
    save_expenses_to_file(expense, expense_file_path)

    #Read file and summarize
    summarize_expense(expense_file_path, budget)


def get_user_expense():
    expense_name = input("Enter Expense Name:\n")
    expense_amount = float(input("Enter Expense Amount:\n"))
    # expense_name = input("Enter Expense Name:\n")
    print(f"Getting user expenses. the expense is {expense_name} and it's {expense_amount}")

    expense_category = ["Food","Rent","Transport","Misc"]

    while True:
        print(f"Select Category: ")
        for i, category_name in enumerate(expense_category):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_category)}]"
        selected_category = int(input(f"Select a category number: {value_range}:\n")) -1


        if selected_category in range(len(expense_category)):
            selected_category_name = expense_category[selected_category]
            new_expense = Expense(name=expense_name, amount=expense_amount, category=selected_category_name)
            return new_expense
        else:
            print("Invalid input. Try again!")


def save_expenses_to_file(expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path ,budget):
    print(f"Summarizing user expenses of {expense_file_path}")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(',')
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("amount_by_category")
    for key, amount in amount_by_category.items():
        print(f"  {key}:  ${amount:.2f}")

    total_cost = sum([expense.amount for expense in expenses])
    print(f"Your total mothly cost is: {total_cost:.2f}$")

    remaining_budget = budget - total_cost
    print(f"Remaining Budget: {remaining_budget:.2f}$")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"{remaining_days} left in this month")

    daily_budget = remaining_budget / remaining_days
    print(f"Your Daily Budget For This Month Is {daily_budget:.2f}$")


if __name__ == "__main__":
    main()