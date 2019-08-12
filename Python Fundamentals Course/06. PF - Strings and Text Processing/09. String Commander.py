initial_string = input()
command = input().split()

result = initial_string
while command[0] != 'end':
    if command[0] == 'Left':
        for roll in range(int(command[1])):
            result = result[1:] + result[0]
    elif command[0] == 'Right':
        for roll in range(int(command[1])):
            result = result[-1] + result[:-1]
    elif command[0] == 'Insert':
        result = result[0:int(command[1])] + command[2] + result[int(command[1]):]
    elif command[0] == 'Delete':
        result = result.replace(result[int(command[1]):(int(command[2]) + 1)], "")

    command = input().split()

print(result)
