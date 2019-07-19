data_list = list(input().lower().split(' '))

data_dict = {}

for i in data_list:
    if data_list.count(i) % 2 == 1:
        data_dict[i] = data_list.count(i)

print(', '.join(data_dict.keys()))
