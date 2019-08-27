import re

kv_pattern = r"(^|(?<=&))(.+\?)?(%20|\+| )*?(?P<key>.+?)(%20|\+| )*?=(%20|\+| )*(?P<value>.+?)(%20|\+| )*?($|(?=&))"
white_space_pattern = r"((%20|\+){2,})|(%20|\+){1}"
ignore_pattern = r"(.+\?)"
while True:
    data_dict = {}
    command = input()
    if command == 'END':
        exit()
    else:
        command = re.sub(white_space_pattern, " ", command)
        for match in re.finditer(kv_pattern, command):
            groups = match.groupdict()
            if groups['key'] not in data_dict.keys():
                data_dict[groups['key']] = []
            data_dict[groups['key']].append(groups['value'])

    for k, v in data_dict.items():
        print(f"{k}=[{', '.join(v)}]", end="")
    print()


