"""
Program: sphereMath.py
Author: Nikolay Skomorohov

Calculate a sphere's diameter, circumference, surface area & volume.
Based on radius.

1. Input - float point:
            radius
2. Formulas for the various calculations
            diameter
            circumference
            surface area
            volume
3. Output the calculations5
"""

# Ask for radius input:
radius = float(input("Enter the radius: "))

# Calculate the metrics:
diameter = radius * 2
circumference = 2 * 3.14 * radius
surface_area = 4 * 3.14 * radius ** 2
volume = 4 / 3 * 3.14 * radius ** 3

# Print the formulas' output:
print("The sphere's metrics are as follows:")
print("The diameter is " + str(diameter))
print("The circumference is " + str(circumference))
print("The volume is " + str(volume))
print("The surface area is " + str(surface_area))
