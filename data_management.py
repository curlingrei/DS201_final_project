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


def view_all_transactions(df):
    print("--- All Transactions ---")
    ## get index start with 1
    df.index = range(1, len(df) + 1)
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
  ## get index start with 1
  transactions.index = range(1, len(transactions) + 1)
  if len(transactions) == 0:
    print("No transactions found in this date range.")
  else:
    print(transactions)

#Add a Transaction: Add a new transaction with details like date, category,description, and amount.
import pandas as pd
transactions = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])
def add_transaction(transactions_df, date, category, description, amount):
    data = {'Date': [date], 'Category': [category], 'Description': [description], 'Amount': [amount]
    }
    new_transaction = pd.DataFrame(data)
    if transactions_df.empty:
        transactions_df =  new_transaction
    else:
        transactions_df = pd.concat([transactions_df, new_transaction], ignore_index=True)
    return transactions_df

transactions = add_transaction(transactions,"2025-03-03", "food", "pizza", 20.80)
print (transactions)

#Edit a Transaction: Modify details of an existing transaction (date,category, description, amount).
def edit_transaction (transactions):
    print("\n view all transactions")
    print(transactions)
while True:
    search_term = input("Enter the search term:").strip().lower()
    filtered_df = transactions[transactions.apply(lambda row: search_term.lower() in str(row.values).lower(), axis=1)]
    if not filtered_df.empty:
        print("transactions found.")
        print(filtered_df)
        break
    else:
        print("No transactions found.")
try:
    index = int(input("Enter the transaction that you want to edit:"))
    if index not in transactions.index:
        print ("not found, try again")
    else:
        print ("currently values")
        print (transactions.loc[index])
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
    transactions.loc[index, "Date"] = new_date
if new_category:
    transactions.loc[index, "Category"] = new_category
if new_description:
    transactions.loc[index, "Description"] = new_description
if new_amount:
    try:
        transactions.loc[index, "Amount"] = float(new_amount)
    except ValueError:
        print("Invalid, try again")
if new_type:
    transactions.loc[index, "Type"] = new_type
    print ("\nTransaction updated")


view_all_transactions = edit_transaction(transactions)

#Delete a Transaction: Remove a specific transaction by its index.
def delete_transaction (transactions):
    print("\n view all transactions")
    print(transactions)
    try:
        index = int(input("Enter the transaction that you want to delete:"))
        if index not in transactions.index:
            print ("not found, try again")
        transactions = transactions.drop(index)
        print ("trasaction deleted successfully")
    except ValueError:
        print ("invalid input, please try again")
    return transactions


