import re

pattern = r"\b(0x)??([0-9A-F]+)\b"
numbers_input = input()
matches = re.finditer(pattern, numbers_input)
for match in matches:
    print(match.group(), end=" ")

