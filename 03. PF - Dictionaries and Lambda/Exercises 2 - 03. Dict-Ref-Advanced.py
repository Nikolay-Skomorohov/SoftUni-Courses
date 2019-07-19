input_list = list(input().split(" -> "))

data_dict = {}

while input_list[0] != "end":
    if input_list[0] not in data_dict.keys():
        if input_list[1].isalpha() and input_list[1] not in data_dict.keys():
            pass
        elif input_list[1].isalpha() and input_list[1] in data_dict.keys():
            data_dict[input_list[0]] = data_dict[input_list[1]].copy()
        elif not input_list[1].isalpha():
            data_dict[input_list[0]] = list(input_list[1].split(", "))
    elif input_list[0] in data_dict.keys():
        if input_list[1].isalpha() and input_list[1] in data_dict.keys():
            data_dict[input_list[0]] = data_dict[input_list[1]].copy()
        elif input_list[1].isalpha() and input_list[1] not in data_dict.keys():
            pass
        elif not input_list[1].isalpha():
            data_dict[input_list[0]].extend(list(input_list[1].split(", ")))
    input_list = list(input().split(" -> "))

for k, v in data_dict.items():
    print(f"{k} === {', '.join(v)}")
