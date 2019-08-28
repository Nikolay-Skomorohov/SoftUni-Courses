import re

p_tag_pattern = r"(<p>(.+?)</p>)"
replace_pattern = r"([^a-z0-9])"
whitespace_pattern = "([ ]{2,})"
result_string = ""
input_string = input()

for tag in re.finditer(p_tag_pattern, input_string):
    add_string = re.sub(replace_pattern, " ", str(tag.group(2)))
    add_string = re.sub(whitespace_pattern, " ", add_string)
    result_string += add_string

print_string = ""

for ch in result_string:
    if ord(ch) in range(97, 110):
        add_letter = chr(ord(ch) + 13)
        print_string += add_letter
    elif ord(ch) in range(110, 123):
        add_letter = chr(ord(ch) - 13)
        print_string += add_letter
    else:
        print_string += ch

print(print_string)
