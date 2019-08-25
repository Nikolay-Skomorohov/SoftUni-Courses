import re

pattern = r"\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z]{1}[a-z]{2})\2(?P<year>[0-9]{4})\b"
input_dates = input()
matches = re.finditer(pattern, input_dates)
for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
