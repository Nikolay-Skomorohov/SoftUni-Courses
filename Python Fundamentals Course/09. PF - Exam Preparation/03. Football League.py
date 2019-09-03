import re


def decrypt_command(team1: str, team2: str, key: str):
    new_command = []
    pattern = rf"(.*?)(?P<key1>({key})+)(?P<name>.+?)(?P<key2>{key}+)(.*)"
    try:
        team_1 = re.search(pattern, team1).group('name')
        new_command.append(team_1[::-1].upper())
        team_2 = re.search(pattern, team2).group('name')
        new_command.append(team_2[::-1].upper())
    except AttributeError:
        pattern = rf'[{key}].*[{key}]'
        team_1 = re.search(pattern, team1).group()
        team_1 = team_1.replace(key, "")
        new_command.append(team_1[::-1].upper())
        team_2 = re.search(pattern, team2).group()
        team_2 = team_2.replace(key, "")
        new_command.append(team_2[::-1].upper())
    return new_command


def print_standing(score_data_dict: dict):
    print("League standings:")
    # data_dict_sorted = sorted(data_dict.items(), key=lambda x: x[1])
    counter = 1
    for value in sorted(score_data_dict.items(), key=lambda x: (-x[1], x)):
        print(f"{counter}. {value[0]} {value[1]}")
        counter += 1


def print_top_goals(goals_data_dict: dict):
    print("Top 3 scored goals:")
    counter = 1
    for team in sorted(goals_data_dict.items(), key=lambda x: (-x[1], x)):
        print(f"- {team[0]} -> {team[1]}")
        counter += 1
        if counter > 3:
            break


def main():
    encryption_key = input()
    score_data_dict = {}
    goals_data_dict = {}

    while True:
        command = input().split()
        if command[0] == 'final':
            break
        else:
            team_list = decrypt_command(command[0], command[1], encryption_key)
            match_result = list(map(int, command[2].split(':')))
            for team in team_list:
                if team not in score_data_dict.keys():
                    score_data_dict[team] = 0
                    goals_data_dict[team] = 0
            if match_result[0] > match_result[1]:
                score_data_dict[team_list[0]] += 3
                score_data_dict[team_list[1]] += 0
            elif match_result[0] == match_result[1]:
                score_data_dict[team_list[0]] += 1
                score_data_dict[team_list[1]] += 1
            elif match_result[0] < match_result[1]:
                score_data_dict[team_list[0]] += 0
                score_data_dict[team_list[1]] += 3
            goals_data_dict[team_list[0]] += match_result[0]
            goals_data_dict[team_list[1]] += match_result[1]

    print_standing(score_data_dict)
    print_top_goals(goals_data_dict)


if __name__ == '__main__':
    main()
