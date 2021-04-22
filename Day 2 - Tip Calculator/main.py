print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
tipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
splitBill = int(input("How many people to split the bill? "))

totalPay = ((totalBill * (1 + (tipPercent / 100))) / splitBill)
roundedPay = round(totalPay, 2)

print("Each person should pay: $" + str(roundedPay))
