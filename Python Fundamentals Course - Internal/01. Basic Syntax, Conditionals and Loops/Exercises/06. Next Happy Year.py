number = int(input())

while True:
    match = False
    number += 1
    for digit in range(len(str(number))):
        for char in range(len(str(number))):
            if digit != char:
                if str(number)[digit] == str(number)[char]:
                    match = True
    if match is False:
        print(f"{number}")
        break









