from collections import deque


def people_input():
    males = deque([int(x) for x in input().split()])
    females = deque([int(x) for x in input().split()])
    return males, females


def check_values(human: int):
    if not human > 0:
        return False
    else:
        return True


def check_values2(human: int):
    if human % 25 == 0:
        return True
    else:
        return False


def print_output(matches: int, males: deque, females: deque):
    print(f"Matches: {matches}")
    if males:
        result = ", ".join(reversed(list(map(str, males))))
        print(f"Males left: {result}")
    else:
        print(f"Males left: none")
    if females:
        result = ", ".join(map(str, females))
        print(f"Females left: {result}")
    else:
        print(f"Females left: none")


def main():
    matches = 0
    males, females = people_input()
    while males and females:
        if check_values(males[-1]):
            pass
        else:
            del males[-1]
            continue
        if check_values(females[0]):
            pass
        else:
            del females[0]
            continue
        if check_values2(males[-1]):
            del males[-1]
            try:
                del males[-1]
            except IndexError:
                pass
            continue
        else:
            pass
        if check_values2(females[0]):
            del females[0]
            try:
                del females[0]
            except IndexError:
                pass
            continue
        else:
            pass
        if males[-1] == females[0]:
            matches += 1
            males.pop()
            females.popleft()
        else:
            females.popleft()
            males[-1] -= 2
    print_output(matches, males, females)


if __name__ == '__main__':
    main()
