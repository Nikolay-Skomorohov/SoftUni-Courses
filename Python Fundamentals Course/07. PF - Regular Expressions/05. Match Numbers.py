import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
input_string = input()
matches = re.finditer(pattern, input_string)
for item in matches:
    print(item.group(), end=" ")
