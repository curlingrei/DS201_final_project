import data_management as dm
import pandas as pd

def main():
    print("=== Personal Finance Tracker ===")
    menus = [
        "Import a CSV File",
        "View All Transactions",
        "View Transactions by Date Range",
        "Add a Transaction",
        "Edit a Transaction",
        "Delete a Transaction",
        "Analyze Spending by Category",
        "Calculate Average Monthly Spending",
        "Show Top Spending Category",
        "Visualize Monthly Spending Trend",
        "Save Transactions to CSV",
        "Exit"]

    for index in range(len(menus)):
        print(f"{index + 1}. {menus[index]}")

    choice = input(f"Choose an option (1-{len(menus)})): ")

    if choice not in list(map(str, range(1, len(menus) + 1))):
      print(f"Invalid input! You need to input a number from 1~{len(menus)}")

    if choice == "1":
      data = dm.import_csv("sample_data.csv")
      print(data)

if __name__ == "__main__":
    main()
