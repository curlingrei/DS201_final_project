## This module is responsible for
## 1. import csv files
## 2. view transactions
## 3. add transactions
## 4. edit transactions
## 5. delete transactions

import pandas as pd
import os

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
    dataframe = pd.read_csv(file_path)
    columns = dataframe.columns.values
    if pd.Series(columns).equals(pd.Series(['Date', 'Category', 'Description', 'Amount', 'Type'])):
      return pd.read_csv(file_path)
    else:
      print("The file doesn't have proper columns")



