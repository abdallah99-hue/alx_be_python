income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
monthly_saving = income - expenses
print("Monthly saving is:", monthly_saving)
interest_rate = 0.05
projected_savings = monthly_saving * 12 * (1 + interest_rate)
print("Projected savings after one year, with interest is:", projected_savings)
