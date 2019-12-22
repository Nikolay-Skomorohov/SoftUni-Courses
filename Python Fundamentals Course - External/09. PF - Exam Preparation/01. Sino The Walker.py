def calculate_needed_time(number_of_steps, step_duration):
    needed_time_total_sec = number_of_steps * step_duration
    days_needed = needed_time_total_sec // 86400
    hours_needed = (needed_time_total_sec % 86400) // 3600
    mins_needed = ((needed_time_total_sec % 86400) % 3600) // 60
    secs_needed = (((needed_time_total_sec % 86400) % 3600) % 60) % 60
    time_needed = [days_needed, hours_needed, mins_needed, secs_needed]
    return time_needed


def print_result(leave_time, time_needed):
    arrival_hour = leave_time[0]
    arrival_min = leave_time[1]
    arrival_sec = leave_time[2]

    arrival_sec += time_needed[3]
    if arrival_sec > 59:
        arrival_sec -= 60
        arrival_min += 1
    arrival_min += time_needed[2]
    if arrival_min > 59:
        arrival_min -= 60
        arrival_hour += 1
    arrival_hour += time_needed[1]
    if arrival_hour > 23:
        arrival_hour -= 24

    if arrival_hour == 0:
        arrival_hour = '00'
    elif arrival_hour < 10:
        arrival_hour = f"0{arrival_hour}"
    if arrival_min == 0:
        arrival_min = '00'
    elif arrival_min < 10:
        arrival_min = f"0{arrival_min}"
    if arrival_sec == 0:
        arrival_sec = '00'
    elif arrival_sec < 10:
        arrival_sec = f"0{arrival_sec}"

    print(f"Time Arrival: {arrival_hour}:{arrival_min}:{arrival_sec}")


def main():
    leave_time = [int(x) for x in input().split(':')]
    number_of_steps = int(input())
    step_duration = int(input())
    total_time_sec = calculate_needed_time(number_of_steps, step_duration)
    print_result(leave_time, total_time_sec)


if __name__ == "__main__":
    main()
