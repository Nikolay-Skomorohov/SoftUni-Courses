'''
Program: piAprox.py
Author: NSS

Calculate the approximation of PY using the Leibniz method and user input.

1. User input
     leibniz
     iterations
2. Calculation formula
     iterCount
     iterNum
     iterOp
     iterCal
     pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
     pi/4 = 1 - 1/n+2 + 1/n+2 -
3. Print the output
     piApprox
'''

# Constants
leibniz = 3.14/4

# User input for the number of iterations
iterations = int(input("Enter the number of iterations: "))

# Calculations

iterCount = 0
iterNum = 1
iterOp = 1
iterCal = 1
while iterCount <= iterations:
    iterCount += 1
    if iterOp == 1:
        iterNum += 2
        iterCal -= (1 / iterNum)
        iterOp = 2
    elif iterOp == 2:
        iterNum += 2
        iterCal += (1 / iterNum)
        iterOp = 1


print(iterCal == leibniz)
print(iterCal)
print(iterCal * 4)
