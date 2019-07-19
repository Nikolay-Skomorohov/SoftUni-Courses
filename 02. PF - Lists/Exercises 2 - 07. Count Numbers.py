list_ints = list(map(int, input().split()))

new_set = set(list_ints)

for item in sorted(new_set):
    print(f"{item} -> {list_ints.count(item)}")
