
import json
from datetime import datetime

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    return expenses

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def add_expense(expenses):
    title = input("Enter the expense title: ")
    amount = float(input("Enter the expense amount: "))
    date = datetime.now().strftime("%Y-%m-%d")
    expense = {"title": title, "amount": amount, "date": date}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def list_expenses(expenses):
    print("Expenses:")
    for index, expense in enumerate(expenses):
        title = expense["title"]
        amount = expense["amount"]
        date = expense["date"]
        print(f"{index + 1}. {title} - ${amount:.2f} - {date}")

def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ${total:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            print("Exiting Expense Tracker...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
