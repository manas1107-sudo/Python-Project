# Python-Project
Personal Finance Manager with Expense Prediction
OVERVIEW

This project is a command-line Personal Finance Manager built with Python. It allows users to record income and expenses, view summaries, visualize monthly spending, and predict next month’s total expense using a simple machine learning model (linear regression).

FEATURES

Add income and expense transactions with date, category, description, and amount.

Store all transactions in a CSV file for easy access and backup.

View overall summary: total income, total expense, and current balance.

View category-wise expense totals.

Display the last 10 transactions.

Plot monthly expenses using a line chart.

Train a basic regression model on past monthly expenses and predict next month’s total expense.


PROJECT STRUCTURE

finance_manager.py – Main Python script containing:

Data initialization and CSV handling

Functions for adding and viewing transactions

Functions for summaries and plotting

Machine learning logic for expense prediction

transactions.csv – Data file automatically created to store all transactions.


TECHNOLOGIES USED

Python 3.x

pandas – for data handling and analysis

scikit-learn – for building the linear regression model

matplotlib – for plotting monthly expenses

CSV file – as a simple data storage solution


INSTALLATION

Make sure Python 3 is installed on your system.

Install the required Python packages:

bash
pip install pandas scikit-learn matplotlib
Place finance_manager.py in a folder where you want to store your project and data files.


HOW IT WORKS

When the program starts, it checks if transactions.csv exists; if not, it creates one with the required columns.

The user interacts with a text-based menu to:

Add income or expense entries

View overall financial summary

View recent transactions

Plot monthly expenses

Predict next month’s total expense

For prediction:

The program aggregates all expenses by month.

Each month is converted to a numeric index.

A linear regression model is trained on historical monthly totals.

The model then predicts the expense for the next month’s index.


USGAE

Run the application from the terminal:

bash
python finance_manager.py
You will see a menu like:

Add transaction

View summary

View last 10 transactions

Plot monthly expenses

Predict next month expense

Exit

Enter the appropriate option number and follow the prompts.

Adding a Transaction
Choose option 1 (Add transaction).

Enter:

Date in YYYY-MM-DD format (or press Enter for today’s date)

Type: income or expense

Category: e.g., Food, Rent, Salary

Description: a short note about the transaction

Amount: numeric value

Viewing Summary
Choose option 2 (View summary).

The program will display:

Total income

Total expense

Current balance

Category-wise expense totals

Viewing Last 10 Transactions
Choose option 3.

The program will show the most recent 10 transactions with their details.

Plotting Monthly Expenses
Choose option 4.

A line chart window will open showing total expenses per month.

This helps visualize spending trends over time.

Predicting Next Month’s Expense
Choose option 5.

The program will:

Train a linear regression model on past monthly expense totals.

Show the model’s R² score on test data (for evaluation).

Display the predicted total expense for the next month.

Note: At least 3 months of expense data are needed for the prediction to work meaningfully.

Example Use Case
A user records daily expenses (Food, Transport, Rent, etc.) and income (Salary, Freelancing, etc.).

At the end of each month, the user checks:

How much was spent in each category.

The overall balance.

The app plots monthly expenses and predicts the next month’s total expense, helping the user plan their budget.
