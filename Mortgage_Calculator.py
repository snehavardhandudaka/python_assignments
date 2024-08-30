def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
    return monthly_payment

principal = float(input("Enter the loan amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years: "))

monthly_payment = calculate_mortgage(principal, annual_rate, years)
print(f"Monthly Payment: ${monthly_payment:.2f}")
