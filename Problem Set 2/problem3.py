monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
original = balance

while upperBound - lowerBound > 0.1:
    minPayment = round((lowerBound + upperBound) / 2, 2)
    balance = original

    for month in range(12):
        balance -= minPayment
        interest = balance * (annualInterestRate / 12)
        balance += interest

    if balance > 0: lowerBound = minPayment
    elif balance < 0: upperBound = minPayment

print("Lowest Payment:", round(minPayment, 2))