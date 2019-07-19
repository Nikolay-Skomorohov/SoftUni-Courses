input_list = list(input().split(" = "))

data_dict = {}

while input_list[0] != "end":
    if input_list[1].isdigit():
        data_dict[input_list[0]] = int(input_list[1])
    else:
        if input_list[1] in data_dict.keys():
            data_dict[input_list[0]] = data_dict[input_list[1]]

    input_list = list(input().split(" = "))

for k, v in data_dict.items():
    print(f"{k} === {v}")
