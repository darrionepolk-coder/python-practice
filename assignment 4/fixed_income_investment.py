# Fixed-Income Investment Revenue Calculator
# This program is for a beginner Python student.
# It asks for valid input values, then calculates monthly investment growth.

while True:
    monthly_investment = float(input("Enter monthly investment amount: "))
    if (monthly_investment := monthly_investment) > 0:
        break
    print("Error: Monthly investment must be positive.")

while True:
    yearly_interest_rate = float(input("Enter yearly interest rate (%): "))
    if (yearly_interest_rate := yearly_interest_rate) > 0:
        break
    print("Error: Yearly interest rate must be positive.")

while True:
    investment_years = int(input("Enter number of years: "))
    if (investment_years := investment_years) > 0:
        break
    print("Error: Number of years must be a positive integer.")

# Convert yearly rate into monthly rate.
monthly_rate = (yearly_interest_rate / 100) / 12

# Start with zero money saved.
balance = 0.0

# Repeat month by month for the full investment years.
for year in range(investment_years):
    for month in range(12):
        balance = balance + monthly_investment
        balance = balance * (1 + monthly_rate)

# Print final result.
print(f"Total investment revenue: ${balance:.2f}")
print(f"Monthly revenue: ${balance / (investment_years * 12):.2f}")
