#setting input of monthly_income & expenses
monthly_income = int(input("Enter your monthly income:"))
monthly_expense = int(input("Enter your total monthly expenses:"))
#Calculate monthly_savings
monthly_savings = monthly_income - monthly_expense
#calculate annualy saving without interest
annual_savings = monthly_savings * 12
#initialize annual_interest
annual_interest = 0.05
#Calculate  annualy saving with interst
annual_savings_interest = monthly_savings * 12 * annual_interest
#Calculate projected saving
projected_savings = annual_savings + annual_savings_interest
#Print the monthly saving and projected saving
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
