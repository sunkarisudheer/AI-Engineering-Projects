from datetime import date
from tabulate import tabulate


def add_expense(expenses: list[dict]) -> None:
    """Add a new expense to the list."""

    print("\n➕ Add New Expense")

    amount_str = input("Enter amount: ").strip()
    category = input("Enter category: ").strip()
    description = input("Enter description (optional): ").strip()

    # Validate amount
    if not amount_str:
        print("❌ Amount cannot be empty.")
        return

    try:
        amount = float(amount_str)
    except ValueError:
        print("❌ Amount must be a valid number.")
        return

    if amount <= 0:
        print("❌ Amount must be greater than 0.")
        return

    if amount > 1_000_000:
        print("⚠️ Amount looks unusually large. Please verify.")
        return

    # Validate category
    if not category.strip():
        print("❌ Category cannot be empty.")
        return

    expense = {
        "date": str(date.today()),
        "amount": amount,
        "category": category.title(),
        "description": description
    }

    expenses.append(expense)

    print("✅ Expense added successfully.")




def list_expenses(expenses: list[dict]) -> None:
    """Display all recorded expenses in table format."""

    if not expenses:
        print("\n📭 No expenses recorded yet.")
        return

    rows = []

    for e in expenses:
        rows.append([
            e.get("date", "N/A"),
            f"₹{e.get('amount', 0):.2f}",
            e.get("category", "N/A"),
            e.get("description", "")
        ])

    print("\n📊 All Expenses\n")
    print(tabulate(rows,
                   headers=["Date", "Amount", "Category", "Description"],
                   tablefmt="grid"))
    


def show_total(expenses: list[dict]) -> None:
    """Calculate and display total spending."""

    if not expenses:
        print("\n📭 No expenses available to calculate total.")
        return

    total = sum(float(e.get("amount", 0)) for e in expenses)

    print(f"\n💰 Total spending: ₹{total:.2f}")



def show_category_summary(expenses: list[dict]) -> None:
    """Display total spending grouped by category."""

    if not expenses:
        print("\n📭 No expenses found.")
        return

    summary = {}

    for e in expenses:
        cat = e.get("category", "Unknown")
        amt = float(e.get("amount", 0))

        summary[cat] = summary.get(cat, 0) + amt

    rows = []

    for cat, amt in summary.items():
        rows.append([cat, f"₹{amt:.2f}"])

    print("\n📊 Category Summary\n")
    print(tabulate(rows, headers=["Category", "Total"], tablefmt="grid"))