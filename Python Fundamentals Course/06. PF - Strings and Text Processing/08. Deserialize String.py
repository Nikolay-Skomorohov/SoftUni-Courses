input_list = input().split(':')

build_string = {}

while input_list[0] != 'end':
    input_char = input_list[0]
    input_char_indexes = input_list[1].split('/')
    for index in input_char_indexes:
        build_string[int(index)] = input_char
    input_list = input().split(':')

result = ""
for key in sorted(build_string.keys()):
    result += build_string[key]

print(result)
