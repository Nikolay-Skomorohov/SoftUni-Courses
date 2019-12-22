import re

happy_pattern = r"([:;]{1}[D\)\*\]\}]{1})|([\(\*c\[]{1}[:;]{1})"
sad_pattern = r"([:;]{1}[\(\[\{c]{1})|([D\)\]]{1}[;:]{1})"

input_string = input()

happy_matches = len(list(re.finditer(happy_pattern, input_string)))
sad_matches = len(list(re.finditer(sad_pattern, input_string)))

happy_index = happy_matches / sad_matches
if happy_index >= 2:
    print(f"Happiness index: {happy_index:.2f} :D")
elif 1 < happy_index < 2:
    print(f"Happiness index: {happy_index:.2f} :)")
elif happy_index == 1:
    print(f"Happiness index: {happy_index:.2f} :|")
elif happy_index < 1:
    print(f"Happiness index: {happy_index:.2f} :(")
print(f"[Happy count: {happy_matches}, Sad count: {sad_matches}]")
