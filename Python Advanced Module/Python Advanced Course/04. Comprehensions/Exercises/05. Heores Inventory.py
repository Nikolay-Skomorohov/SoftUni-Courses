heroes_list = {name: {} for name in input().split(", ")}

while 1:
    command = input().split("-")
    if command[0] == "End":
        break
    else:
        if not command[0] in heroes_list:
            continue
        elif command[1] in heroes_list[command[0]]:
            continue
        else:
            heroes_list[command[0]][command[1]] = int(command[2])

print(*[f"{x} -> Items: {len(heroes_list[x])}, Cost: {sum(i for z, i in heroes_list[x].items())}" for x, y in heroes_list.items()], sep="\n")
