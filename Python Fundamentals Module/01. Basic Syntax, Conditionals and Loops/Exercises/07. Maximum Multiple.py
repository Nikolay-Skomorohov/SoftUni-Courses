divisor = int(input())
bound = int(input())
largest = None

for n in range(1, bound + 1):
    if n % divisor == 0:
        largest = n

print(largest)
