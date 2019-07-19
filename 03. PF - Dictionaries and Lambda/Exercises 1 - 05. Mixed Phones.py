input_list = list(input().split(" : "))

data_dict = {}

while input_list[0] != "Over":
    if input_list[0].isdigit():
        data_dict[input_list[1]] = input_list[0]
    else:
        data_dict[input_list[0]] = input_list[1]

    input_list = list(input().split(" : "))

for k, v in sorted(data_dict.items()):
    print(f"{k} -> {v}")
