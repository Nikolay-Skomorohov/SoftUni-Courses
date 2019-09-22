input_list = [int(x) for x in input().split()]
count = 0
while True:
    command = input().split()

    if command[0] == "set":
        new_set = list(set(input_list))
        if sorted(new_set) == sorted(input_list):
            print("It is a set")
        else:
            print(new_set)
    elif command[0] == "filter":
        new_list = []
        if command[1] == "odd":
            new_list = [x for x in input_list if x % 2 == 1]
        elif command[1] == "even":
            new_list = [x for x in input_list if x % 2 == 0]
        if len(new_list) > 0:
            print(new_list)
    elif command[0] == "multiply":
        print(list([x * int(command[1]) for x in input_list]))
    elif command[0] == "divide":
        if int(command[1]) == 0:
            print("ZeroDivisionError caught")
        else:
            new_list = [x / int(command[1]) for x in input_list]
            print(list(new_list))
    elif command[0] == "slice":
        if (len(input_list) - 1) < int(command[1]) or (len(input_list) - 1) < int(command[2]):
            print("IndexError caught")
        else:
            print(input_list[int(command[1]):int(command[2])])
    elif command[0] == "sort":
        print(list(sorted(input_list)))
    elif command[0] == "reverse":
        print(list(reversed(input_list)))
    elif command[0] == "exhausted":
        print(f"I beat It for {count} rounds!")
        break
    count += 1
