Personal Expense Tracker
Overview

The Personal Expense Tracker is a simple command-line application built with Python that helps users track and manage their daily expenses.
The program allows users to record expenses, view all transactions, calculate total spending, and generate category-based summaries.

This project demonstrates basic software design, modular programming, and file-based data persistence using JSON.

Features
Add a new expense with amount, category, and description
View all recorded expenses
Calculate total spending
Display spending summary by category
Persist expense data using a JSON file
Menu-driven command line interface

Personal-Expense-Tracker
│
├── src
│   ├── main.py        # Entry point of the application
│   ├── tracker.py     # Core expense tracking logic
│   └── storage.py     # Handles file read/write operations
│
├── data
│   └── sample_expenses.json   # Example expense data
│
├── .gitignore
└── README.md


How the Application Works
1. Add Expense
   Users can enter:
   amount
   category (Food, Travel, Bills, etc.)
   description

The program saves this data to a JSON file.

2. View Expenses
   Displays a list of all expenses stored in the system.

   Example output:

   Date        Category    Amount    Description
   ------------------------------------------------
   2026-03-10  Food        250       Lunch
   2026-03-10  Travel      100       Bus


3. Total Spending
   Calculates the sum of all recorded expenses.

   Example:
   Total Spending: ₹350

4. Category Summary
   Shows how much money was spent in each category.

   Example:
   Food   : ₹250
   Travel : ₹100
   Technologies Used


5. Save teh data into the json file
   
   
Technologies Used
  Python 3
  JSON for lightweight data storage
  Command Line Interface (CLI)

How to Run
  Navigate to the project directory:  cd Personal-Expense-Tracker/src
  Run the program: python main.py