import json
import os
from datetime import datetime

DATA_FILE = 'data.json'

# Load existing data or initialize
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Save data
def save_data(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

# Add new expense
def add_expense(amount, category, description):
    expenses = load_data()
    expense = {
        'amount': float(amount),
        'category': category,
        'description': description,
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    expenses.append(expense)
    save_data(expenses)
    print("✅ Expense added successfully.")

# View all expenses
def view_expenses():
    expenses = load_data()
    if not expenses:
        print("No expenses recorded.")
        return
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['description']}")

# Total expenses
def total_expenses():
    expenses = load_data()
    total = sum(e['amount'] for e in expenses)
    print(f"💰 Total Expenses: ₹{total}")

# Filter by category
def filter_by_category(cat):
    expenses = load_data()
    filtered = [e for e in expenses if e['category'].lower() == cat.lower()]
    for e in filtered:
        print(f"{e['date']} | ₹{e['amount']} | {e['description']}")

# Menu
def menu():
    while True:
        print("\n📊 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Filter by Category")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amt = input("Enter amount: ₹")
            cat = input("Enter category: ")
            desc = input("Enter description: ")
            add_expense(amt, cat, desc)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            total_expenses()

        elif choice == '4':
            cat = input("Enter category to filter: ")
            filter_by_category(cat)

        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
