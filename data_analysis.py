import data_management as dm
import matplotlib.pyplot as plt
import pandas as pd
import calendar

csv_file_name = "sample_data.csv"
df = dm.import_csv("sample_data.csv")

#total amount per category
total_by_category = df.groupby("Category")["Amount"].sum()

# def choose_display(dis)

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


#Calculate Average Monthly Spending
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['month_name'] = df['Month'].apply(lambda x: calendar.month_name[x])

monthly_spending = df.groupby("month_name")["Amount"].sum()
print(monthly_spending)

average_monthly_spending = monthly_spending.mean()
print(f"Your average monthly spending is {average_monthly_spending:.2f}")




