def stack_n():
    result = []
    number = int(input())
    for num in range(number):
        command = list(map(int, input().split(" ")))
        if command[0] == 1:
            result.append(command[1])
        elif result and command[0] == 2:
            result.pop()
        elif result and command[0] == 3:
            print(max(result))
        elif result and command[0] == 4:
            print(min(result))
    return ", ".join(map(str, reversed(result)))


print(stack_n())

# to_print = stack_n()
#
# while to_print:
#     if not len(to_print) == 1:
#         print(f"{to_print.pop()}", end=", ")
#     elif len(to_print) == 1:
#         print(f"{to_print.pop()}")
#     else:
#         print("")


