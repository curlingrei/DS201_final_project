import data_management as dm
import data_analysis as da
import pandas as pd

def main():
    csv_file_name = "sample_data.csv"
    df = dm.import_csv("sample_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])

    print("=== Personal Finance Tracker ===")
    print(f"Note: Current data was imported from {csv_file_name}.")

    menus = [
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
        dm.view_all_transactions(df)
    elif choice == "2":
        dm.view_transactions_by_date_range(df)
    elif choice == "6":
        da.spending_total_by_category(df)
    elif choice == "8":
        da.show_top_category(df)


if __name__ == "__main__":
    main()
