numbers = input()
list_number = numbers.split()
list_number = list(map(float, list_number))

while True:
    no_more = None
    for i in range(len(list_number) - 1):
        if list_number[i] == list_number[i+1]:
            list_number[i] += list_number[i]
            list_number.pop(i+1)
            no_more = False
            break
        elif i == 0:
            no_more = True
        else:
            no_more = True
    if no_more or len(list_number) < 2:
        print(*list_number)
        break
