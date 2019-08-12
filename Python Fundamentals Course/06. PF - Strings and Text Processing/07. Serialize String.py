input_string = [x for x in input()]
char_data_dict = {}

for char in input_string:
    char_data_dict[char] = []
    count = 0
    for symbol in input_string:
        if char == symbol:
            char_data_dict[char].append(str(count))
        count += 1

for k, v in char_data_dict.items():
    char_list = '/'.join(v)
    print(f"{k}:{char_list}")
