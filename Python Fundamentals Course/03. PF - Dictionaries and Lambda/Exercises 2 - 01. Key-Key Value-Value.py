key = input()
value = input()
num = abs(int(input()))

data_dict = {}

for i in range(num):
    input_list = list(input().split(' => '))
    input_values = input_list[1].split(";")

    if key in input_list[0]:
        data_dict[input_list[0]] = []

    for item in input_values:
        if value in item and key in input_list[0]:
            data_dict[input_list[0]].append(item)

for k, v in data_dict.items():
    print(f"{k}:")
    for el in v:
        print(f"-{el}")
