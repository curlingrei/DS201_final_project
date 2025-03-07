import data_management as dm
import matplotlib.pyplot as plt
import pandas as pd

csv_file_name = "sample_data.csv"
df = dm.import_csv("sample_data.csv")

#total amount per category
def spending_total_by_category(df):
    if 'Category' not in df.columns or 'Amount' not in df.columns:
        return

    total_by_category = df.groupby("Category")["Amount"].sum()


    def absolute_value(val):
        total = sum(total_by_category)
        absolute = int(val/100 * total)
        return f"{absolute}"

    ax = total_by_category.plot(kind = 'pie',
                      autopct= absolute_value,
                      startangle=90,
                      ylabel="",
                      legend=False)
    ax.set_title("Spending by Category")
    print(total_by_category)
    plt.show()



