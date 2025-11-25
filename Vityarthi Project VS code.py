import os
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

DATA_FILE = "transactions.csv"


def init_data_file():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["date", "type", "category", "description", "amount"])
        df.to_csv(DATA_FILE, index=False)


def load_data():
    init_data_file()
    df = pd.read_csv(DATA_FILE)
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
    return df


def save_data(df):
    df.to_csv(DATA_FILE, index=False)


def add_transaction():
    print("\nAdd New Transaction")
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if date_str == "":
        date = datetime.today().date()
    else:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Using today's date instead.")
            date = datetime.today().date()

    t_type = input("Type (income/expense): ").strip().lower()
    if t_type not in ["income", "expense"]:
        print("Invalid type. Defaulting to 'expense'.")
        t_type = "expense"

    category = input("Category (e.g., Food, Rent, Salary): ").strip()
    description = input("Description: ").strip()

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Invalid amount. Transaction cancelled.")
        return

    df = load_data()
    new_row = {
        "date": date.strftime("%Y-%m-%d"),
        "type": t_type,
        "category": category,
        "description": description,
        "amount": amount,
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    print("Transaction added successfully.")


def view_summary():
    df = load_data()
    if df.empty:
        print("\nNo transactions yet.")
        return

    total_income = df[df["type"] == "income"]["amount"].sum()
    total_expense = df[df["type"] == "expense"]["amount"].sum()
    balance = total_income - total_expense

    print("\n==== Overall Summary ====")
    print(f"Total income : {total_income:.2f}")
    print(f"Total expense: {total_expense:.2f}")
    print(f"Balance      : {balance:.2f}")

    print("\n==== Category-wise Expense ====")
    expense_by_cat = df[df["type"] == "expense"].groupby("category")["amount"].sum()
    if expense_by_cat.empty:
        print("No expenses recorded.")
    else:
        for cat, amt in expense_by_cat.items():
            print(f"{cat}: {amt:.2f}")


def view_transactions():
    df = load_data()
    if df.empty:
        print("\nNo transactions to display.")
        return

    print("\nLast 10 transactions:")
    print(df.sort_values("date", ascending=False).head(10).to_string(index=False))


def plot_monthly_expenses():
    df = load_data()
    if df.empty:
        print("\nNo data to plot.")
        return

    df_expense = df[df["type"] == "expense"].copy()
    if df_expense.empty:
        print("\nNo expenses to plot.")
        return

    df_expense["year_month"] = df_expense["date"].dt.to_period("M")
    monthly = df_expense.groupby("year_month")["amount"].sum().reset_index()
    monthly["year_month"] = monthly["year_month"].astype(str)

    plt.figure(figsize=(8, 4))
    plt.plot(monthly["year_month"], monthly["amount"], marker="o")
    plt.xticks(rotation=45)
    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.tight_layout()
    plt.show()


def prepare_time_series_for_prediction():
    df = load_data()
    df_expense = df[df["type"] == "expense"].copy()
    if df_expense.empty:
        return None

    df_expense["year_month"] = df_expense["date"].dt.to_period("M")
    monthly = df_expense.groupby("year_month")["amount"].sum().reset_index()
    monthly["year_month"] = monthly["year_month"].astype(str)

    # Use month index as simple numeric feature
    monthly
