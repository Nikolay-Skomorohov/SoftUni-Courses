input_list = list(map(int, input().split(" ")))

for index in range(len(input_list)):
    if input_list[index] > 0:
        input_list[index] = -input_list[index]
    elif input_list[index] == 0:
        continue
    elif input_list[index] < 0:
        input_list[index] = abs(input_list[index])
print(input_list)