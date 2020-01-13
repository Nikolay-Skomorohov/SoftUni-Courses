energy = 100
coins = 100

input_list = input().split("|")

for event in input_list:
    item = event.split("-")
    if item[0] == "rest":
        if energy < 100:
            for i in range(1, int(item[1]) + 1):
                energy += 1
                if energy == 100 or i == int(item[1]):
                    print(f"You gained {i} energy.")
                    print(f"Current energy: {energy}.")
                    break
                else:
                    continue
            # add = 100 - energy
            # if int(item[1]) > add:
            #     energy += add
            #     print(f"You gained {add} energy.")
            # elif int(item[1]) <= add:
            #     energy += int(item[1])
            #     print(f"You gained {int(item[1])} energy.")
        elif energy >= 100:
            print(f"You gained 0 energy.")
            print(f"Current energy: {energy}.")
    elif item[0] == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += int(item[1])
            print(f"You earned {int(item[1])} coins.")
        elif (energy - 30) < 0:
            energy += 50
            print(f"You had to rest!")
    else:
        if (coins - int(item[1])) > 0:
            coins -= int(item[1])
            print(f"You bought {item[0]}.")
        else:
            print(f"Closed! Cannot afford {item[0]}.")
            closed = True
            exit()

print(f"Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
