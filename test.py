import data_management as dm
import pandas as pd

# data = pd.read_csv("sample_data.csv")
data = dm.import_csv("sample_data.csv")
print(data)
