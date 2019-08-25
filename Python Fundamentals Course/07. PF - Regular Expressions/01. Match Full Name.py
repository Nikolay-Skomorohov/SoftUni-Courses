import re

name_pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"

input_names = input()

matches = re.findall(name_pattern, input_names)
for item in matches:
    print(item, end=" ")
