input_list = input().split(":")

data_dict = {}
pass_dict = {}

while input_list[0] != "ready":
    if input_list[0] not in data_dict.keys():
        data_dict[input_list[0]] = {}
    vehicle_list = input_list[1].split(",")
    for veh in vehicle_list:
        type_cap = veh.split("-")
        data_dict[input_list[0]][type_cap[0]] = int(type_cap[1])

    input_list = input().split(":")

second_command = input().split(" ")

while second_command[0] != "travel":
    pass_dict[second_command[0]] = int(second_command[1])
    second_command = input().split(" ")

for city in pass_dict.keys():
    if pass_dict[city] <= sum(data_dict[city].values()):
        print(f"{city} -> all {pass_dict[city]} accommodated")
    elif pass_dict[city] > sum(data_dict[city].values()):
        print(f'''{city} -> all except {pass_dict[city]
                        - abs(sum(data_dict[city].values()))} accommodated''')
