'''
Program: investment.py
Author: Ken
Compute an investment report.

1. The inputs are:
    starting investment amount
    number of years
    interest rate (an integer percent)
2. The report is displayed in tabular from with a header.
3. Computations and outputs:
    for each year
       compute the interest and ad it to the investment
       print a formatted row of results for that year
4. The ending investment and the interest earned are alose displayed
'''

# Accept the inputs
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

# Convert the rate to a decimal number
rate = rate / 100

# Initialize the accumulator for the interest
totalInterest = 0.0

# Dispaly the header for the table
print("%4s%22s%16s%20s" %
      ("Year", "Starting balance",
       'Interest', "Ending balance"))

# Compute and display the results for each year
for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%22.2f%16.2f%20.2f" %
          (year, startBalance, interest, endBalance))
    startBalance = endBalance
    totalInterest += interest

# Dispaly the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)
