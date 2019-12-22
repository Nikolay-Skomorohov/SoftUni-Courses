input_list = input().split(" -> ")

data_dict = {}

while input_list[0] != "filter":
    if input_list[0] not in data_dict.keys():
        data_dict[input_list[0]] = []
    for i in input_list[1].split(", "):
        if i not in data_dict[input_list[0]]:
            data_dict[input_list[0]].append(i)

    input_list = input().split(" -> ")

input_tags_list = input().split(", ")

for k, v in data_dict.items():
    if all(x in v for x in input_tags_list):
        result = ['#' + x for x in v]
        print(f"{k} | {', '.join(result)}")
