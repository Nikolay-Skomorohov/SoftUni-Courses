import re

text_string = input()

diamond_pattern = r"<.*?>"
diamonds_found = re.findall(diamond_pattern, text_string)
diamonds_list = []
for diamond_string in diamonds_found:
    carat_sum = 0
    for char in diamond_string:
        if char.isdigit():
            carat_sum += int(char)
    if carat_sum > 0:
        diamonds_list.append(carat_sum)

if len(diamonds_list) > 0:
    for dia in diamonds_list:
        print(f"Found {dia} carat diamond")
else:
    print("Better luck next time")

