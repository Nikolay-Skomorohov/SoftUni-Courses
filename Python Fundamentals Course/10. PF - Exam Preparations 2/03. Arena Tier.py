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
                    for skill in gladiator_dict[command[0]].keys():
                        if any(x == skill for x in gladiator_dict[command[1]].keys()):
                            gladiator1_points = 0
                            for skl in gladiator_dict[command[0]].keys():
                                gladiator1_points += gladiator_dict[command[0]][skl]
                            gladiator2_points = 0
                            for skl in gladiator_dict[command[1]].keys():
                                gladiator2_points += gladiator_dict[command[1]][skl]

                            if gladiator1_points > gladiator2_points:
                                del gladiator_dict[command[1]]
                            elif gladiator1_points < gladiator2_points:
                                del gladiator_dict[command[0]]

    print(gladiator_dict)


if __name__ == "__main__":
    main()
