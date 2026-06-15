import json
from datetime import date

FILE_NAME = "expenses.json"


def get_all_expenses() -> list:
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def update_expenses(data: list) -> None:
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def view_all_expenses() -> None:
    data = get_all_expenses()

    if not data:
        print("No expenses found!")
        return

    print("\n")
    print(f"{'ID':<5}{'DATE':<15}{'CATEGORY':<20}{'AMOUNT'}")
    print("-" * 50)

    for item in data:
        print(
            f"{item['id']:<5}"
            f"{item['Date']:<15}"
            f"{item['Category']:<20}"
            f"{item['Amount']}"
        )

    print()


def add_expense() -> None:
    data = get_all_expenses()

    expense = {}

    expense["id"] = 1 if not data else data[-1]["id"] + 1

    while True:
        category = input("Enter Category: ").strip()

        if category:
            expense["Category"] = category
            break

        print("Category cannot be empty!")

    while True:
        try:
            amount = float(input("Enter Amount: "))

            if amount <= 0:
                print("Amount must be positive!")
                continue

            expense["Amount"] = amount
            break

        except ValueError:
            print("Please enter a valid amount!")

    expense["Date"] = str(date.today())

    data.append(expense)
    update_expenses(data)

    print("Expense added successfully!")


def delete_expense() -> None:
    data = get_all_expenses()

    if not data:
        print("No expenses available!")
        return

    try:
        expense_id = int(input("Enter Expense ID: "))

        original_length = len(data)

        data = [expense for expense in data if expense["id"] != expense_id]

        if len(data) == original_length:
            print("Expense not found!")
            return

        update_expenses(data)

        print("Expense deleted successfully!")

    except ValueError:
        print("Please enter a valid ID!")


def total_expenses() -> None:
    data = get_all_expenses()

    total = sum(expense["Amount"] for expense in data)

    print(f"\nTotal Spending: ₹{total:.2f}\n")


def category_report() -> None:
    data = get_all_expenses()

    if not data:
        print("No expenses found!")
        return

    report = {}

    for expense in data:
        category = expense["Category"]

        report[category] = (
            report.get(category, 0)
            + expense["Amount"]
        )

    print("\nCategory Wise Report")
    print("-" * 30)

    for category, amount in report.items():
        print(f"{category:<15} ₹{amount:.2f}")

    print()


def main():
    while True:
        print("\n" + "=" * 55)
        print("          EXPENSE TRACKER")
        print("=" * 55)

        print("1. View All Expenses")
        print("2. Add Expense")
        print("3. Delete Expense")
        print("4. Total Spending")
        print("5. Category Report")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                view_all_expenses()

            elif choice == 2:
                add_expense()

            elif choice == 3:
                delete_expense()

            elif choice == 4:
                total_expenses()

            elif choice == 5:
                category_report()

            elif choice == 6:
                print("Thank you for using Expense Tracker!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    main()