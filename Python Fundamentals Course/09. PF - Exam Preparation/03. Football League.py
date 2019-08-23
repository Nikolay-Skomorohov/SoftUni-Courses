import re

decrypt_key = input()
team_pattern = rf'[{decrypt_key}].*[{decrypt_key}]'
line_of_code = input().split()
teams_dict_points = {}
teams_dict_goals = {}

while line_of_code[0] != 'final':
    score = line_of_code[2].split(':')

    team_1 = re.search(team_pattern, line_of_code[0]).group()
    team_1 = team_1.replace(decrypt_key, "")
    team_1 = team_1[::-1].upper()
    if team_1 not in teams_dict_points.keys():
        teams_dict_points[team_1] = 0
        teams_dict_goals[team_1] = 0
    if int(score[0]) > int(score[1]):
        teams_dict_points[team_1] += 3
    elif score[0] == score[1]:
        teams_dict_points[team_1] += 1
    teams_dict_goals[team_1] += int(score[0])

    team_2 = re.search(team_pattern, line_of_code[1]).group()
    team_2 = team_2.replace(decrypt_key, "")
    team_2 = team_2[::-1].upper()
    if team_2 not in teams_dict_points.keys():
        teams_dict_points[team_2] = 0
        teams_dict_goals[team_2] = 0
    if int(score[0]) < int(score[1]):
        teams_dict_points[team_2] += 3
    elif score[0] == score[1]:
        teams_dict_points[team_2] += 1
    teams_dict_goals[team_2] += int(score[1])

    line_of_code = input().split()

print('League standings:')
counter = 1
for k, v in sorted(teams_dict_points.items(), key=lambda x: x[1], reverse=True):
    print(f"{counter}. {k} {v}")
    counter += 1

print('Top 3 scored goals:')
counter = 1
for k, v in sorted(teams_dict_goals.items(), key=lambda x: x[1], reverse=True):
    print(f"- {k} -> {v}")
    counter += 1
    if counter > 3:
        break
