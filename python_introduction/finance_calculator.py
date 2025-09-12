income = float(input("Enter your monthly income:"))

expenses = float(input("Enter your total monthly expenses:"))

monthy_savings = income - expenses

projected_savings = monthy_savings * 12 + (monthy_savings * 12 * 0.05)

print("Your monthly savings are:", monthy_savings)
print("Projected savings after one year, with interest, is: ", projected_savings)