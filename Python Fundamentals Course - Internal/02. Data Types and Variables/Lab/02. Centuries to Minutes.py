number = int(input())

centuries = number
years = centuries * 100
days = round(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{number} centuries = {years} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")
