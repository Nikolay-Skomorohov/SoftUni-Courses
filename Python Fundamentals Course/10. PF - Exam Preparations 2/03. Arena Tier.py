def main():
    gladiator_dict = {}
    while True:
        command = input()
        if command == "Ave Cesar":
            break
        else:
            if "->" in command:
                command = command.split(" -> ")
                if command[0] not in gladiator_dict.keys():
                    gladiator_dict[command[0]] = {}
                if command[1] not in gladiator_dict[command[0]][command[1]]:
                    gladiator_dict[command[0]][command[1]] = int(command[2])
                else:
                    if int(command[2]) > gladiator_dict[command[0]][command[1]]:
                        gladiator_dict[command[0]][command[1]] = command[2]

            elif " vs " in command:
                command = command.split(" vs ")
                if command[0] in gladiator_dict.keys() and command[1] in gladiator_dict.keys():


if __name__ == "__main__":
    main()
