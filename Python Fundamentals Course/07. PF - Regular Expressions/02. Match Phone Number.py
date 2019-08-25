import re

pattern = r"(\+359)(-| )2\2(\d{3})\2(\d{4})\b"

phones_input = input()

matches = re.finditer(pattern, phones_input)
for match in matches:
    print(match.group(), end=" ")