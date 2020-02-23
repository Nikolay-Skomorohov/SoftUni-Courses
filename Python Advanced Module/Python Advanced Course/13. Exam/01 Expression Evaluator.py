import math

def input_func():
    initial_string = input().split(" ")
    return initial_string


def to_multi(*args):
    temp = args[0][0]
    for num in args[0][1:]:
        temp *= num
    return temp


def to_sum(*args):
    return sum(args[0])


def to_sub(*args):
    temp = args[0][0]
    for num in args[0][1:]:
        temp -= num
    return temp


def to_div(*args):
    temp = args[0][0]
    for num in args[0][1:]:
        temp /= num
    return math.floor(temp)


def main():
    the_string = input_func()
    result = None
    stack = []
    for ch in the_string:
        if not ch in ("*", "+", "-", "/"):
            stack.append(int(ch))
        else:
            if ch == "*":
                result = to_multi(stack)
                stack = []
            elif ch == "+":
                result = to_sum(stack)
                stack = []
            elif ch == "-":
                result = to_sub(stack)
                stack = []
            elif ch == "/":
                result = to_div(stack)
                stack = []
            stack.append(result)
    print(*stack)


if __name__ == '__main__':
    main()
