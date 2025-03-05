## This module is responsible for
## 1. import csv files
## 2. view transactions
## 3. add transactions
## 4. edit transactions
## 5. delete transactions

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




