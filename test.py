import data_management as dm
import pandas as pd
import matplotlib.pyplot as plt

df = dm.import_csv("sample_data.csv")
print(df)

spending = df[~df['Category'].isin(["Income"])]['Amount'].sum()
print(spending)
income = df[df['Category'] == "Income"]['Amount'].sum()
print(income)

balance = pd.DataFrame({'Category': ['income', 'spending'], 'total_value': [income, spending]}).reset_index(drop=True)
print(balance)

pie_chart = balance.plot(kind="pie", y="total_value", labels=balance['Category'])
pie_chart.set_ylabel("")
plt.title("The proportion of total amount by categories")
pie_chart.legend(title="Category", loc="center left", bbox_to_anchor=(0.9, 0.8))
plt.show()