import pandas as pd
import matplotlib.pyplot as plt

def compare_balance(df):
    spending = df[~df['Category'].isin(["Income"])]['Amount'].sum()
    income = df[df['Category'] == "Income"]['Amount'].sum()

    balance = pd.DataFrame({'Category': ['income', 'spending'], 'total_value': [income, spending]}).reset_index(
        drop=True)

    pie_chart = balance.plot(kind="pie", y="total_value", labels=balance['Category'])
    pie_chart.set_ylabel("")
    plt.title("The proportion of total amount by categories")
    pie_chart.legend(title="Category", loc="center left", bbox_to_anchor=(0.9, 0.8))
    plt.show()

