import re

old_pattern = re.compile(r"(^|(?<=\s)*)(<a[ ]?href=)(.+)(\>)(.+)(\<\/a\>)")
new_pattern = re.compile(r"(\[URL href=)(.+)(\])(.+)(\[\/URL\])")

command = input()

while command != "end":
    if old_pattern.search(command):
        old_string = old_pattern.search(command)
        add_string = f"{old_string.group(1)}[URL href={old_string.group(3)}]{old_string.group(5)}[/URL]"
        command = command.replace(old_string.group(), add_string)
    print(command)
    command = input()
