import json
import os

# Determine project base directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Data folder
DATA_DIR = os.path.join(BASE_DIR, "data")

# JSON file path
file_path = os.path.join(DATA_DIR, "expenses.json")


def data_file_exists() -> None:
    """
    Ensure the data directory and file exist.
    If not, create them with an empty list.
    """

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(file_path):
        print("📁 Expense file not found. Creating new file...")
        with open(file_path, "w") as file:
            json.dump([], file)


def load_file() -> list[dict]:
    """Load expenses from JSON file."""

    data_file_exists()

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("⚠️ File is corrupted. Resetting expenses file.")
        return []
    except Exception as e:
        print(f"⚠️ Error loading file: {e}")
        return []


def save_expenses(expenses: list[dict]) -> None:
    """Save all expenses to JSON file."""

    data_file_exists()

    try:
        with open(file_path, "w") as file:
            json.dump(expenses, file, indent=4)

    except Exception as e:
        print(f"❌ Failed to save expenses: {e}")