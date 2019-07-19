list_ints = list(map(int, input().split()))
new_list = []
sorted_elem = 0

for num in range(sorted_elem + 1, len(list_ints)):

    for se in range(0, sorted_elem + 1):

        if list_ints[se] > list_ints[num]:
            pos_new = list_ints[num]
            list_ints.pop(num)
            list_ints.insert(se, pos_new)
            break
    sorted_elem += 1

print(*list_ints)
