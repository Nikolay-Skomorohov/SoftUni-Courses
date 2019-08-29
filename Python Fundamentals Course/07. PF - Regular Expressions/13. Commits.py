import re

pattern = r"https://github\.com/(?P<user>[A-Za-z0-9\-]+)/(?P<repo>[a-zA-Z-_]+)/commit/(?P<hash>[0-9a-f]{40}),(?P<message>[^(\n]+),(?P<add>[0-9]+),(?P<del>[0-9]+)"
data_dict = {}
total_dict = {}
while True:
    command = input()
    if command == "git push":
        break
    elif re.fullmatch(pattern, command):
        string = re.fullmatch(pattern, command)
        if string.group('user') not in data_dict.keys():
            data_dict[string.group('user')] = {}
            total_dict[string.group('user')] = {}
        if string.group('repo') not in data_dict[string.group('user')].keys():
            data_dict[string.group('user')][string.group('repo')] = {}
            total_dict[string.group('user')][string.group('repo')] = {'add': 0, 'del': 0}
        data_dict[string.group('user')][string.group('repo')][string.group('hash')] = f"commit {string.group('hash')}: {string.group('message')} ({string.group('add')} additions, {string.group('del')} deletions)"
        total_dict[string.group('user')][string.group('repo')]['add'] += int(string.group('add'))
        total_dict[string.group('user')][string.group('repo')]['del'] += int(string.group('del'))
    else:
        pass

for usr, val1 in sorted(data_dict.items()):
    print(f"{usr}:")
    for rep in sorted(val1.keys()):
        print(f"  {rep}:")
        for val2 in data_dict[usr][rep].values():
            print(f"    {val2}")
        print(f"    Total: {total_dict[usr][rep]['add']} additions, {total_dict[usr][rep]['del']} deletions")
