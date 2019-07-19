input_string = input()

data_string = {}

for i in input_string:
    data_string[i] = input_string.count(i)

for k, v in data_string.items():
    print(f"{k} -> {v}")
