import data_management as dm
import data_analysis as da
import visualization as vi
import budget_management as bm
import pandas as pd

def main():
    csv_file_name = "sample_data.csv"
    df = dm.import_csv("sample_data.csv")
    df['Date_month'] = df['Date'].str.split(pat="-", expand=True)[1]
    df['Date'] = pd.to_datetime(df['Date'])
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

    while True:
        print("=== Personal Finance Tracker ===")
        print(f"Note: Current data was imported from {csv_file_name}.")

        for index in range(len(menus)):
            print(f"{index + 1}. {menus[index]}")

        choice = input(f"Choose an option (1-{len(menus)})): ")

        if choice not in list(map(str, range(1, len(menus) + 1))):
            print(f"Invalid input! You need to input a number from 1~{len(menus)}")

        if choice == "1":
            dm.view_all_transactions(df)
        elif choice == "2":
            dm.view_transactions_by_date_range(df)
        elif choice == "3":
            df = dm.add_transaction(df)
        elif choice == "4":
            dm.edit_transaction(df)
        elif choice == "5":
            df = dm.delete_transaction(df)
        elif choice == "6":
            da.spending_total_by_category(df)
        elif choice == "7":
            da.monthly_spending_average(df)
        elif choice == "8":
            da.show_top_category(df)
        elif choice == "9":
            vi.select_chart(df)
        elif choice == "10":
            dm.export_csv(df)
        elif choice == "11":
            bm.compare_balance(df)
        elif choice =="12":
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break

if __name__ == "__main__":
    main()
