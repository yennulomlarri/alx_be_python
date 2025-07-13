# finance_calculator.py

# Prompt the user for their monthly income and convert it to a float.
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses and convert it to a float.
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings.
monthly_savings = monthly_income - monthly_expenses

# Calculate the projected annual savings with interest.
# Formula: (Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Display the user's monthly savings.
print(f"Your monthly savings are ${monthly_savings}.")

# Display the projected annual savings.
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")