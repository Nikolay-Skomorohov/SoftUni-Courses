'''
Program: rightTriangle.py
Author: NSS

Program that checks if a triangle is a right triable
based on input for the 3 sides.

1. The inputs are:
    side1
    side2
    side3
2. Check if the triangle is right or not
    side1 = side2 ** 2 + side3 ** 2
3. Output should state whether the triangle is right or not
    output
'''

import math

# Inputs for the trianble's sides
side1 = float(input("Enter the length of a side: "))
side2 = float(input("Enter the length of another side: "))
side3 = float(input("Enter the length of the last side: "))

# Check if one of the sides matches the condition for a right triangle
if (round(math.sqrt(side2 ** 2 + side3 ** 2)) == side1) or \
   (round(math.sqrt(side1 ** 2 + side3 ** 2)) == side2) or \
   (round(math.sqrt(side1 ** 2 + side2 ** 2)) == side3):
    print("The specified figure is a right triangle.")
else:
    print("The specified figure is NOT a right triangle.")
