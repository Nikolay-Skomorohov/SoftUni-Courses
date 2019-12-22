def print_result(inventory: list):
    print(*inventory)


def main():
    inventory = input().split()
    while True:
        command = input().split()
        if command[0] == "Buy" and command[1] not in inventory:
            inventory.append(command[1])
        elif command[0] == "Trash" and command[1] in inventory:
            inventory.remove(command[1])
        elif command[0] == "Repair" and command[1] in inventory:
            inventory.remove(command[1])
            inventory.append(command[1])
        elif command[0] == "Upgrade":
            update = command[1].split("-")
            if update[0] in inventory:
                inventory.insert((inventory.index(update[0]) + 1), f"{update[0]}:{update[1]}")
        elif command[0] == "Fight!":
            break
    print_result(inventory)


if __name__ == "__main__":
    main()
