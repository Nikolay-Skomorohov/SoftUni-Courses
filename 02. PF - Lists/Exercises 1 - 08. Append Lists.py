list_numbers = list(reversed(input().split("|")))
new_list = []
for i in list_numbers:
    new_list.extend(i.split())

print(*new_list)
