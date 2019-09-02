import re


def decrypt_command(team1: str, team2: str, key: str):
    new_command = []
    pattern = rf"(.*?)(?P<key1>[{key}]+)(?P<name>.+?)(?P<key2>[{key}]+)(.*)"
    team_1 = re.search(pattern, team1).group('name')
    new_command.append(team_1[::-1])
    team_2 = re.search(pattern, team2).group('name')
    new_command.append(team_2[::-1])
    return new_command


def print_standing(data_dict: dict):
    print("League standings:")
    # data_dict_sorted = sorted(data_dict.items(), key=lambda x: x[1])
    for k, v in enumerate(sorted(data_dict.items(), key=lambda x: x[1]), 1):
        print(f"{k}. {v[0].upper()} {v[1]}")


def print_top_goals(data_dict: dict):
    count = 1
    print("Top 3 scored goals:")
    for team in sorted(data_dict, key=lambda x: x[1]):
        print(f"- {team[0].upper()} -> {team[1]}")
        count += 1
        if count > 3:
            break


def main():
    encryption_key = input()
    data_dict = {}

    while True:
        command = input().split()
        if command[0] == 'final':
            break
        else:
            team_list = decrypt_command(command[0], command[1], encryption_key)
            match_result = list(map(int, command[2].split(':')))
            for team in team_list:
                if team not in data_dict.keys():
                    data_dict[team] = {'points': 0, 'goals': 0}
                if match_result[0] > match_result[1]:
                    data_dict[team]['points'] += 3
                elif match_result[0] == match_result[1]:
                    data_dict[team]['points'] += 1
            data_dict[team_list[0]]['goals'] += match_result[0]
            data_dict[team_list[1]]['goals'] += match_result[1]

    print_standing(data_dict)
    print_top_goals(data_dict)


if __name__ == '__main__':
    main()
