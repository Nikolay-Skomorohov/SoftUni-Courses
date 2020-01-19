from collections import deque
capacity = int(input())

names = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        names.append(command)

while names:
    command = input()
    if not command.startswith("refill"):
        person = names.popleft()
        if int(command) <= capacity:
            capacity -= int(command)
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    else:
        capacity += int(command.split(" ")[1])

print(f"{capacity} liters left")

