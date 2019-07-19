import re

employees_list = list(input().split(' -> '))

data_dict = {"Age": {}, "Salary": {}, "Position": {}}

while employees_list[0] != 'filter base':
    try:
        if re.search(r"[-]?\d+\.\d+", employees_list[1]):

            data_dict["Salary"][employees_list[0]] = employees_list[1]

        else:
            raise ValueError
    except ValueError:
        try:
            if re.search(r"[-]?\d+", employees_list[1]):
                data_dict["Age"][employees_list[0]] = employees_list[1]
            else:
                raise ValueError
        except ValueError:
            data_dict["Position"][employees_list[0]] = employees_list[1]

    employees_list = list(input().split(' -> '))

sort_by_command = input()

for k, v in data_dict[sort_by_command].items():
    print(f"Name: {k}")
    print(f"{sort_by_command}: {v}")
    print("====================")
