"""
Program: newEncrypt.py
Author: NSS

Program that encypts a numeric value via Caesar cipher and bit shift.

1. User input
     user_number
2. Encrypt the user input
     num_ecrypt
     user_convert
3. Print the result
     user_encrypt
"""

# User input - integer
user_number = input("Enter a text for encryption: ")

# Convert the user input
num_encrypt = ""
for num in user_number:
    num_ASCII = int(ord(num) + 1)
    num_binary = ""
    while num_ASCII > 0:
        remainder = num_ASCII % 2
        num_ASCII = num_ASCII // 2
        num_binary = str(remainder) + num_binary
    num_shift = num_binary[1:] + num_binary[0]
    num_encrypt += num_shift + " "

user_encrypt = num_encrypt + "!"

# Print the result
print(f"The encryption result is {user_encrypt}")
