employee_name = input("Employee's name: ")

number_of_shifts = int(input("Number of Shifts: "))
number_of_transactions = int(input("Number of Transactions: "))
transaction_dollar_value = float(input("Transaction dollar value: "))

productivity_score = (transaction_dollar_value/ number_of_transactions) / number_of_shifts

if productivity_score <= 30:
    bonus = 50.00
else:
    if productivity_score <= 69:
        bonus = 75.00
    else:
        if productivity_score <= 199:
            bonus = 100.00
        else:
            bonus = 200.00

print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus:.1f}")