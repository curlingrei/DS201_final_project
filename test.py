import data_management as dm
import pandas as pd

data = dm.import_csv("sample_data.csv")
print(data)
data.to_csv("test.csv")
