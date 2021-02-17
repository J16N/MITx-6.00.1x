print("Remaining balance:", round(
    balance * ((1 - monthlyPaymentRate) * (1 + annualInterestRate / 12)) ** 12
, 2))