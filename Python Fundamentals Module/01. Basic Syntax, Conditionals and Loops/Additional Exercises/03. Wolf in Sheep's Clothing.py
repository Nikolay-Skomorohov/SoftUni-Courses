input_list = list(reversed(input().split(", ")))

for index in range(len(input_list)):
    if input_list[index] == "wolf":
        if input_list[index] == input_list[0]:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
