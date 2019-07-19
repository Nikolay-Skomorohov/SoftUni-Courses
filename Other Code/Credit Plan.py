'''
Program: creditPlan.py
Author: NSS

Calculates credit details based on item's purchase price.

1. Input
    buyPrice
2. Constants
    downPay
    yearIntRate
    monthIntRate
3. Calculate the various details
    nowOwed
    monthlyInterest
    monthlyPrincipal
    monthlyPayment
    remainBalance
4. Print the output and format in table
'''

# Input for purchase price
buyPrice = float(input("Enter the purchase price: "))

# Initialize the constants

downPay = buyPrice * 0.10
yearIntRate = 0.12
monthlyPayment = 0.05 * (buyPrice - downPay)


# Calculate the various details
nowOwed = buyPrice - downPay
month = 0
print("%-6s%6s%12s%12s%12s" % ("Month", "Interest", "Principal", "Payment", "Remaining"))
while nowOwed > 0:
    month += 1
    monthlyInterest = (nowOwed * yearIntRate) / 12
    monthlyPrincipal = monthlyPayment - monthlyInterest
    payCurrent = monthlyPrincipal + monthlyInterest
    remainBalance = nowOwed - payCurrent
    print("%-6d%6.1f%12.1f%12.1f%12.1f" %
         (month, monthlyInterest, monthlyPrincipal, payCurrent, remainBalance))
    nowOwed = remainBalance
