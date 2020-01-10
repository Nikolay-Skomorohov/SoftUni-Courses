n = int(input())
capacity = 0

for num in range(n):
    litters_to_pour = int(input())
    if (capacity + litters_to_pour) <= 255:
        capacity += litters_to_pour
    else:
        print("Insufficient capacity!")
print(capacity)