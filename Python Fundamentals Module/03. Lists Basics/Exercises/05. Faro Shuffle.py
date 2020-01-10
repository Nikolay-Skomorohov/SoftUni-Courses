input_list = input().split(" ")
shuffles_number = int(input())

new_list = []

for i in range(shuffles_number):
    first_half = input_list[:int(len(input_list) / 2)]
    second_half = input_list[int(len(input_list) / 2):]
    new_list = []
    for length in range(len(input_list)):
        new_list.append(0)
    for index in range(0, (len(input_list))):
        if index % 2 == 0:
            new_list[index] = first_half[0]
            first_half.pop(0)
        elif index % 2 == 1:
            new_list[index] = second_half[0]
            second_half.pop(0)
    input_list = list(new_list)
print(input_list)