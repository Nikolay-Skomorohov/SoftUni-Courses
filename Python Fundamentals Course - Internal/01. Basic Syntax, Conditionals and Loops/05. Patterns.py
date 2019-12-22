input_number = int(input())

for n in range(1, input_number + 1):
    print("*" * n)
for n in range(input_number - 1, 0, -1):
    print("*" * n)
