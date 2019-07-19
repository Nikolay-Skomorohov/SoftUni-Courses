input_list = list(input().split(' '))

data_dict = {}

while input_list[0] != 'shopping' and input_list[1] != 'time':
    if input_list[1] not in data_dict.keys():
        data_dict[input_list[1]] = int(input_list[2])
    else:
        data_dict[input_list[1]] += int(input_list[2])

    input_list = list(input().split(' '))

output_list = list(input().split(' '))

while output_list[0] != "exam" and output_list[0] != "time":
    if output_list[1] in data_dict.keys():
        data_dict[output_list[1]] -= int(output_list[2])
    elif output_list[1] in data_dict.keys() and data_dict[output_list[1]] <= 0:
        print(f"{data_dict[output_list[1]]} out of stock")
    else:
        print(f"{output_list[1]} doesn't exist")

    output_list = list(input().split(' '))

for k, v in data_dict.items():
    if v > 0:
        print(f"{k} -> {v}")
