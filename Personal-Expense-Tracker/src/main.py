from storage import load_file, save_expenses
from tracker import add_expense, list_expenses, show_category_summary, show_total


def show_menu() -> None:
    """Display the main menu options."""
    print("\n=================================")
    print("        Personal Expense Tracker")
    print("=================================")
    print("1) Add Expense")
    print("2) View All Expenses")
    print("3) Show Total Spending")
    print("4) Category Summary")
    print("5) Save & Exit")
    print("=================================")


def main() -> None:
    """Main program loop."""

    # Load existing expenses from file
    try:
        expenses = load_file()
    except Exception:
        print("⚠️ Could not load expenses file. Starting with empty list.")
        expenses = []

    print("\n📂 Expense tracker started successfully.")

    while True:
        show_menu()

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            list_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            show_category_summary(expenses)

        elif choice == "5":
            save_expenses(expenses)
            print("\n💾 Expenses saved successfully.")
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()