key = int(input())
n = int(input())

message = ""

for char in range(n):
    letter = input()
    message += chr(ord(letter) + key)

print(message)