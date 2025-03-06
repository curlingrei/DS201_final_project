## move codes to data_management later
def export_csv(df):
    while True:
        file_name = input("Enter file name to save (e.g., 'transactions.csv'): ")
        if file_name.endswith(".csv"):
            df.to_csv(file_name, index=False)
            print("Transactions saved to my_transactions.csv successfully!")
            break
        else:
            print("The file format should be csv. Try again.")
            continue