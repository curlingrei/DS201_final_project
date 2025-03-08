## This module is responsible for
## 1. import csv files
## 2. view transactions
## 3. add transactions
## 4. edit transactions
## 5. delete transactions
from operator import index

import pandas as pd
import os
import common
from datetime import datetime

def import_csv(file_path):
  error_code = 0
  if not os.path.exists(file_path):
    error_code =  1
  elif not file_path.endswith(".csv"):
    error_code =  2

  if error_code == 1:
    print("The file doesn't exist")
  elif error_code == 2:
    print("Invalid file format")
  else:
    df = pd.read_csv(file_path)
    columns = df.columns.values
    if pd.Series(columns).equals(pd.Series(['Date', 'Category', 'Description', 'Amount', 'Type'])):
      return pd.read_csv(file_path)
    else:
      print("The file doesn't have proper columns")

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

def view_all_transactions(df):
    print("--- All Transactions ---")
    print(df)

def view_transactions_by_date_range(df):

  while True:
    start_date = input("Enter the start date (YYYY-MM-DD):")
    if common.is_valid_yyyy_mm_dd(start_date):
      break
    else:
      print("You need to input the deadline in YYYY-MM-DD format")
      continue

  while True:
    end_date = input("Enter the end date (YYYY-MM-DD):")

    if common.is_valid_yyyy_mm_dd(end_date):
      if datetime.strptime(start_date, "%Y-%m-%d").date() > datetime.strptime(end_date, "%Y-%m-%d").date():
        print("End date should be after start date")
        continue
      else:
        break
    else:
      print("You need to input the deadline in YYYY-MM-DD format")
      continue

  print(f"--- Transactions from {start_date} to {end_date} ---")
  transactions = df[df['Date'].between(start_date, end_date)]
  if len(transactions) == 0:
    print("No transactions found in this date range.")
  else:
    print(transactions)

def add_transaction(df):
    while True:
        date = input("Enter the date（YYYY-MM-DD）: ")
        if common.is_valid_yyyy_mm_dd(date):
            break
        else:
            print("You need to input the deadline in YYYY-MM-DD format")
            continue

    while True:
        category = input("Enter the category （e.g., Food, Rent）: ")
        if category != "":
            break
        else:
            print("You need to input a category")
            continue

    while True:
        description = input("Enter a description:  ")
        if description != "":
            break
        else:
            print("You need to input a description")
            continue

    while True:
        amount = input("Enter the amount: ")
        if amount != "":
            break
        else:
            print("You need to input amount")
            continue

    while True:
        ts_type = input("Enter the Type（Income or Expense）: ")
        if ts_type != "":
            break
        else:
            print("You need to input type")
            continue

    data = {'Date': [pd.to_datetime(date)], 'Category': [category], 'Description': [description], 'Amount': [amount], 'Type': [ts_type], 'Date_month': [date.split("-")[1]]}
    new_transaction = pd.DataFrame(data)
    if df.empty:
        print("Transaction added successfully!")
        return new_transaction
    else:
        print("Transaction added successfully!")
        return pd.concat([df, new_transaction], ignore_index=True)

#Edit a Transaction: Modify details of an existing transaction (date,category, description, amount).
def edit_transaction(df):
    view_all_transactions(df)
    while True:
        search_term = input("Enter the search term: ").strip().lower()
        filtered_df = df[df.apply(lambda row: search_term.lower() in str(row.values).lower(), axis=1)]
        if not filtered_df.empty:
            print("transactions found.")
            print(filtered_df)
            break
        else:
            print("No transactions found.")
    try:
        index = int(input("Enter the transaction that you want to edit:"))
        if index not in df.index:
            print ("not found, try again")
        else:
            print ("currently values")
            print (df.loc[index])
    except ValueError:
        print ("invalid input, please try again")
    finally:
        print ("Finalizing process")

    new_date = input("Enter the new date (YYYY-MM-DD):")
    new_category = input("Enter the new category:").strip()
    new_description = input("Enter the new description:").strip()
    new_amount = input("Enter the new amount:").strip()
    new_type = input("Enter the new type:").strip()

    if new_date:
        df.loc[index, "Date"] = new_date
    if new_category:
        df.loc[index, "Category"] = new_category
    if new_description:
        df.loc[index, "Description"] = new_description
    if new_amount:
        try:
            df.loc[index, "Amount"] = float(new_amount)
        except ValueError:
            print("Invalid, try again")
    if new_type:
        df.loc[index, "Type"] = new_type
        print ("\nTransaction updated")

#Delete a Transaction: Remove a specific transaction by its index.
def delete_transaction (df):
    view_all_transactions(df)
    try:
        index = int(input("Enter the transaction that you want to delete:"))
        if index not in df.index:
            print ("not found, try again")
        updated_df = df.drop(index)
        print ("The transaction was deleted successfully")
        return updated_df
    except ValueError:
        print ("invalid input, please try again")


