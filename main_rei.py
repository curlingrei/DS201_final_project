import data_management as dm
import visualization as vi
import budget_management as bm
import pandas as pd
import export_csv as ec

def main():
    csv_file_name = "sample_data.csv"
    df = dm.import_csv("sample_data.csv")
    df['Date_month'] = df['Date'].str.split(pat="-", expand=True)[1]
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
        "Compare between income and spending",
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
    elif choice == "9":
        vi.select_chart(df)
    elif choice == "10":
        ## change from ec to vi later
        ec.export_csv(df)
    elif choice == "11":
        ## change from ec to vi later
        bm.compare_balance(df)


if __name__ == "__main__":
    main()
