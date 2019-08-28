import re

pattern = r"(https://github\.com/([A-Za-z0-9\-]+)/([a-zA-Z\-\_]+)/commit/([0-9a-f]{40}),([^(\n]+),([0-9]+),([0-9]+))"
data_dict = {}

while True:
    command = input()
    if command == "git push":
        break
    elif re.fullmatch(pattern, command):
        string = re.fullmatch(pattern, command)
        if string.group('user') not in data_dict.keys():
            data_dict[string.group('user')] = {}
        if string.group('repo') not in data_dict[string.group('user')].keys():
            data_dict[string.group('user')][string.group('repo')] = {}
        data_dict[string.group('user')][string.group('repo')][string.group('hash')] = f"commit {string.group('hash')}: {string.group('message')} ({string.group('add')} additions, {string.group('del')} deletions)"
    else:
        pass

for usr in data_dict.keys():
    print(f"{usr}:")
    for rep in usr.keys():

    print(f"  {us}:")