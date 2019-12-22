list_ints = list(map(int, input().split()))
to_swap = None

while True:
    to_swap = False
    for i in range(len(list_ints)-1):
        if list_ints[i] > list_ints[i+1]:
            new_i = list_ints[i]
            new_i2 = list_ints[i+1]
            list_ints[i] = new_i2
            list_ints[i+1] = new_i
            to_swap = True
    if to_swap is False:
        break

print(*list_ints)
