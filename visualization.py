import pandas as pd
import matplotlib.pyplot as plt
import data_management as dm

def select_chart(df):
    while True:
        chart_number = input("1. Monthly Total Spending 2: Total Spending by Categories 3. The Proportion of Total Spending by Categories. 4. Exit \nSelect a chart by number(1-4): ")
        if chart_number == "1":
            visualize_line(df)
        elif chart_number == "2":
            visualize_bar(df)
        elif chart_number == "3":
            visualize_pie(df)
        elif chart_number == "4":
            break
        else:
            print("Invalid Input! You need to input 1, 2 or 3")

def visualize_line(df):
    monthly_total_amount = df.groupby('Date_month')['Amount'].sum().reset_index()
    monthly_total_amount.plot(kind="line", x="Date_month", y="Amount")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.title("Monthly Total amount")
    plt.show()

def visualize_bar(df):
    total_amount_grouped_by_category = df.groupby('Category')['Amount'].sum()
    total_amount_grouped_by_category.plot(kind="bar")
    plt.xlabel("Categories")
    plt.ylabel("Total Amount")
    plt.title("Total amount by categories")
    plt.show()

def visualize_pie(df):
    total_amount_grouped_by_category = df.groupby('Category')['Amount'].sum()
    pie_chart = total_amount_grouped_by_category.plot(kind="pie")
    pie_chart.set_ylabel("")
    plt.title("The proportion of total amount by categories")
    pie_chart.legend(title="Category", loc="center left", bbox_to_anchor=(0.9, 0.8))
    plt.show()
