# Python-Project
Personal Finance Manager with Expense Prediction


Project Overview
Personal Finance Manager is a command-line application designed to help users track their income and expenses, analyze spending patterns, and predict future expenses using machine learning. The application stores transaction data locally and provides visualization tools to better understand financial habits.
Features

Transaction Management: Add and categorize income and expense transactions with dates and descriptions
Financial Summary: View overall balance, total income, and expenses broken down by category
Transaction History: Display the most recent 10 transactions
Data Visualization: Generate monthly expense trend charts using matplotlib
Expense Prediction: Use linear regression to forecast next month's expenses based on historical data
Persistent Storage: All transactions are saved to a CSV file for long-term tracking

Technologies Used

Python 3.x: Core programming language
pandas: Data manipulation and CSV file handling
scikit-learn: Machine learning library for expense prediction
matplotlib: Data visualization for expense trends
datetime: Date and time handling

Installation and Setup
Prerequisites
Ensure you have Python 3.6 or higher installed on your system.
Step 1: Install Required Libraries
Install all dependencies using pip:
bashpip install pandas scikit-learn matplotlib
Step 2: Download the Script
Save the provided Python script as finance_manager.py in your desired directory.
Step 3: Run the Application
Navigate to the directory containing the script and run:
bashpython finance_manager.py
The application will automatically create a transactions.csv file in the same directory to store your data.
How to Use
When you launch the application, you'll see a menu with the following options:

Add Transaction: Record a new income or expense entry
View Summary: Display total income, expenses, balance, and category-wise breakdown
View Last 10 Transactions: Show recent transaction history
Plot Monthly Expenses: Generate a line chart showing expense trends over time
Predict Next Month Expense: Use machine learning to forecast upcoming expenses
Exit: Close the application

Instructions for Testing
Test Case 1: Adding Transactions

Select option 1 from the menu
Add sample income transactions:

Date: 2025-01-15, Type: income, Category: Salary, Description: Monthly salary, Amount: 5000


Add sample expense transactions:

Date: 2025-01-20, Type: expense, Category: Food, Description: Groceries, Amount: 150
Date: 2025-02-05, Type: expense, Category: Rent, Description: Monthly rent, Amount: 1200
Date: 2025-02-10, Type: expense, Category: Food, Description: Restaurant, Amount: 75



Test Case 2: Viewing Summary

Select option 2 to view the financial summary
Verify that total income, expenses, and balance are calculated correctly
Check that expenses are grouped by category

Test Case 3: Viewing Transactions

Select option 3 to display recent transactions
Verify that transactions appear in reverse chronological order

Test Case 4: Plotting Monthly Expenses

After adding transactions across multiple months, select option 4
A graph window should open displaying monthly expense trends
Close the graph window to return to the menu

Test Case 5: Expense Prediction

Add transactions for at least 3 different months
Select option 5 to predict next month's expenses
Review the R² score and predicted amount
Note: Prediction accuracy improves with more historical data

Test Case 6: Data Persistence

Add several transactions
Exit the application (option 0)
Restart the application
Verify that all previous transactions are still available

File Structure
project-directory/
│
├── finance_manager.py      # Main application script
└── transactions.csv         # Auto-generated data file (created on first run)
Notes

All transaction data is stored locally in transactions.csv
The prediction model requires at least 3 months of expense data for meaningful results
Date format must be YYYY-MM-DD (or press Enter to use today's date)
Transaction amounts should be positive numbers
The application uses a simple linear regression model for predictions

Future Enhancements

Add budget setting and alerts
Support for multiple currencies
Export reports to PDF
More sophisticated prediction models
Database integration for better data management


Author: Manas Gursahani
License: MIT
Version: 1.0.0
