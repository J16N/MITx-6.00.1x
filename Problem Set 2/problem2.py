minMonthlyPaymentRate = 0.02
original = balance
minPayment = int(original * minMonthlyPaymentRate)
minPayment += (10 - minPayment % 10)

while balance > 0:
    balance = original

    for month in range(12):
        balance -= minPayment
        interest = balance * (annualInterestRate / 12)
        balance += interest

    minPayment += 10 if balance > 0 else 0

print("Lowest Payment:", minPayment)