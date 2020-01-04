number = input()

for num in range(1, int(number) + 1):
    total = 0
    for digit in str(num):
        total += int(digit)
    if total == 5 or total == 7 or total == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")