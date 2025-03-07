
import data_management as dm
import matplotlib.pyplot as plt
import pandas as pd


csv_file_name = "sample_data.csv"
df = dm.import_csv("sample_data.csv")

#total amount per category
def spending_total_by_category(df):

    inclusive_df = df[df['Type'] == "Expense"]

    total_by_category = inclusive_df.groupby("Category")["Amount"].sum()

    total_by_category.plot(kind = 'bar',
                                   title = 'Total spending by Category',
                                   color = 'r',
                                    rot = 45)
    print(total_by_category)
    plt.show()





