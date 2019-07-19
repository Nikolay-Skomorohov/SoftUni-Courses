'''
Program: newDecrypt.py
Author: NSS

Program that decrypts a number with Caesar cipher with binary bit shift.

1. User input
     user_input
2. Decrypt the user input
     num_decrypt
3. Print the output
     user_decrypt
'''

# User input
user_input = input("Enter a text for decryption: ").split()

# Decrypt the user input

num_decrypt = ""
for num in user_input:
    if ("0" or "1") in num:
        user_shift = num[-1] + num[:-1]
        exponent = len(num) - 1
        user_decimal = 0
        for ch in user_shift:
            user_decimal = user_decimal + int(ch) * 2 ** exponent
            exponent -= 1
        user_chr = chr(user_decimal - 1)
        num_decrypt += user_chr

print(f"The decrypted text reads as follows: {num_decrypt}")
