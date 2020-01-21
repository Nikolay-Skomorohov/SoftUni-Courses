from collections import deque

pumps = int(input())
pump_info = deque()

for pump in range(pumps):
    pump_info.append(input())

start_index = 0
fuel = 0

while pump_info:
    current = pump_info.popleft()
    pump_stats = current.split(" ")
    fuel += int(pump_stats[0])
    if not pump_info and start_index == 0:
        break
    elif fuel >= int(pump_stats[1]):
        fuel -= int(pump_stats[1])
        continue
    else:
        pump_info.append(current)
        start_index += 1
        fuel = 0
        if start_index == len(pump_info):
            exit()

print(start_index)
