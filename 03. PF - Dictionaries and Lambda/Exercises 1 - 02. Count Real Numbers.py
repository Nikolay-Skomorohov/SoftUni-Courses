data_list = list(map(float, input().split(' ')))

data_dict = {}

for i in data_list:
    data_dict[i] = data_list.count(i)

for key in sorted(data_dict):
    print(f"{key} -> {data_dict[key]} times")
