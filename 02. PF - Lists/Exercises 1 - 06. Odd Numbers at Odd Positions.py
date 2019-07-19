list_numbers = list(map(int, input().split()))

for i in range(len(list_numbers)):
    if i % 2 == 1 and list_numbers[i] % 2 == 1:
        print(f"Index {i} -> {list_numbers[i]}")
