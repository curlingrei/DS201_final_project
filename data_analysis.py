import matplotlib.pyplot as plt
import pandas as pd
import calendar

#total amount per category
def spending_total_by_category(df):
    inclusive_df = df[df['Type'] == "Expense"]
    total_by_category = inclusive_df.groupby("Category")["Amount"].sum()
    total_by_category.plot(kind = 'bar',
                                   title = 'Total spending by Category',
                                   color = 'r',
                                    rot = 45)
    plt.show(block=False)
    input("Enter something: ")

def monthly_spending_average(df):
    inclusive_df = df[df['Type'] == "Expense"]
    total_by_category = inclusive_df.groupby("Category")["Amount"].sum()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['month_name'] = df['Month'].apply(lambda x: calendar.month_name[x])

    monthly_spending = df.groupby("month_name")["Amount"].sum()
    print(monthly_spending)

    monthly_spending.plot(kind = 'bar',
                        title = 'Monthly Spending',
                        x = 'Month',
                        y = 'Amount')
    plt.show(block=False)
    input("Enter something: ")

    average_monthly_spending = monthly_spending.mean()
    print(f"Your average monthly spending is {average_monthly_spending:.2f}")

#Top spending category

    top_spending_category = total_by_category.idxmax()
    print(f"Top Spending Category is {top_spending_category}")

#Top spending category
def show_top_category(df):
    inclusive_df = df[df['Type'] == "Expense"]
    total_by_category = inclusive_df.groupby("Category")["Amount"].sum()
    top_spending_category = total_by_category.idxmax()
    print(f"Top Spending Category is {top_spending_category}")






