'''
Program: growthRate.py
Author: NSS

Calculates the population growth based on initial size,
growth rate and time to achieve it.

1. User inputs
     initialPop - 1000
     growthRate - 10% per h
     growthTime - 1h
     totalTime - 24h
2. Calculate the growth rates
     growthTick = totalPop * growthRate
     totalPop = growthTick * totalTIme
3. Display/print the output
     totalPop
'''

# User inputs
initialPop = int(input("Enter the initial population: "))
growthRate = float(input("Enter the growth rate: "))
growthTime = int(input("Enter the growth time to achieve the growth rate: "))
totalTime = int(input("Enter the total time the population will grow: "))

# Calculate the growth rates
totalPop = initialPop

for tick in range(1, totalTime + 1):
    growthTick = totalPop * growthRate
    totalPop += growthTick

# Print the results
print("The total population after", totalTime, "hours will be", totalPop)
