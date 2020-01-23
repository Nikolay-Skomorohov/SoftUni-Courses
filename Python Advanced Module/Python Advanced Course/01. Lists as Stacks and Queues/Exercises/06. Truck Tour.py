from collections import deque
pumps = int(input())
start_deck = deque()

for pump in range(pumps):
    start_deck.append(input())

it_deck = start_deck.copy()
fuel = 0
index = 0
while it_deck:
    current = it_deck[0].split(" ")
    fuel += int(current[0])
    if fuel >= int(current[1]):
        fuel -= int(current[1])
        it_deck.popleft()
        continue
    else:
        start_deck.append(start_deck.popleft())
        it_deck = start_deck.copy()
        index += 1
        fuel = 0
print(index)