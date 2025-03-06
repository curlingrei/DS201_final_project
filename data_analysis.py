import data_management as dm
import matplotlib.pyplot as plt
import pandas as pd

csv_file_name = "sample_data.csv"
df = dm.import_csv("sample_data.csv")

#total amount per category
total_by_category = df.groupby("Category")["Amount"].sum()

ax = total_by_category.plot(kind = 'pie',
                      autopct="%1.1f%%",
                      startangle=90,
                      ylabel="",
                      legend=False)
print(total_by_category)
ax.set_title("Spending by Category")
plt.show()
