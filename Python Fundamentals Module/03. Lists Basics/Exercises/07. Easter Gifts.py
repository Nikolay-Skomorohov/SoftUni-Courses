gifts_list = input().split(" ")

command = input().split(" ")

while command[0] != "No":
    if command[0] == "OutOfStock":
        for gift in range(len(gifts_list)):
            if gifts_list[gift] == command[1]:
                gifts_list[gift] = None
    elif command[0] == "Required":
        if int(command[2]) in range(0, len(gifts_list)):
            gifts_list[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts_list[-1] = command[1]
    command = input().split(" ")

for item in gifts_list:
    if item is not None:
        print(item, end=" ")
