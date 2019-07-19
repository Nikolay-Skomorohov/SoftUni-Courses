import math

list_numbers = list(map(int, input().split(" ")))

new_list = []

for i in list_numbers:
    if math.sqrt(abs(i)) == int(math.sqrt(abs(i))):
        if i > 0:
            new_list.append(i)

new_list.sort(reverse=True)

print(*new_list)
