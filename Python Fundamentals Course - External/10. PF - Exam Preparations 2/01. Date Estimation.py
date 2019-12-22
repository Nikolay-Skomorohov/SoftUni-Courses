data_dict = {"1": 31,
             "2": 28,
             "22": 29,
             "3": 31,
             "4": 30,
             "5": 31,
             "6": 30,
             "7": 31,
             "8": 31,
             "9": 30,
             "10": 31,
             "11": 30,
             "12": 31}

read_input = list(map(int, input().split('-')))

year_today = 2018
month_today = 8
day_today = 26

year_input = read_input[0]
month_input = read_input[1]
day_input = read_input[2]

current_data = 26
for year in range(year_today):
    if year % 4 == 0 and not year % 100 == 0:
        current_data += 366
    elif year % 100 == 0 and not year % 400 == 0:
        current_data += 365
    elif year % 400 == 0:
        current_data += 366
    else:
        current_data += 365

for month in range(1, month_today):
    current_data += data_dict[str(month)]

other_data = int(day_input)
for year in range(0, year_input):
    if year % 4 == 0 and not year % 100 == 0:
        other_data += 366
    elif year % 100 == 0 and not year % 400 == 0:
        other_data += 365
    elif year % 400 == 0:
        other_data += 366
    else:
        other_data += 365

for month in range(1, month_input):
    other_data += data_dict[str(month)]

result = other_data - current_data
if result == 0:
    print("Today date")
elif result < 0:
    print("Passed")
else:
    print(f"{result + 1} days left")
