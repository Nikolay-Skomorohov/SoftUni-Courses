input_list = list(input().split(" "))

data_dict = {}

while input_list[0] != "Aggregate":
    region = input_list[0]
    size = int(input_list[1])
    if region not in data_dict.keys():
        data_dict[region] = []
    if size not in data_dict[region]:
        data_dict[region].append(size)
    input_list = list(input().split(" "))

for key, val in data_dict.items():
    joined = list(map(str, val))
    result = key + " -> " + ", ".join(joined)
    print(f"{result} ({sum(val) - int(sum(val) / len(val))})")
