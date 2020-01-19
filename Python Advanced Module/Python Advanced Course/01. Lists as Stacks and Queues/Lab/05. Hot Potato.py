from collections import deque

names = deque()
names.extend(input().split(" "))
number = int(input())

while True:
    for i in range(1, number + 1):
        person = names.popleft()
        if i == number:
            if names:
                print(f"Removed {person}")
            else:
                print(f"Last is {person}")
                exit()
        else:
            names.append(person)



