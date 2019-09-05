read_input = list(map(int, input().split('-')))

year_today = 2018
month_today = 8
day_today = 26

year_input = read_input[0]
month_input = read_input[1]
day_input = read_input[2]

if year_input <= year_today:
    if month_input <= month_today:
        if day_input < day_today:
            print('Passed')
        elif day_input == day_today:
            print('1 day left')
        else:
            print(f"{day_today - day_input}")
    else:
        days_difference = day_input - day_today
        months_difference = month_today -
        print(f"{(months_difference * 30) + days_difference} days left")
else:
    days_difference = day_today - day_input
    months_difference = month_today - month_input
    years_difference = year_today - y
    print(f"{(months_difference * 30) + days_difference} days left")