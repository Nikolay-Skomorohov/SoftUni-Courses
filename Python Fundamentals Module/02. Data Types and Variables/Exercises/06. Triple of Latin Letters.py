number = int(input())

for char in range(97, (97 + number)):
    for letter in range(97, (97 + number)):
        for bukva in range(97, (97 + number)):
            print(f"{chr(char)}{chr(letter)}{chr(bukva)}")
