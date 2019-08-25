import re

pattern = r"(([2-9]|10|[JQKA]){1}[SHDC]{1})"
input_cards = input()
matches = re.findall(pattern, input_cards)
for item in matches:
    print(item[0], end=" ")
