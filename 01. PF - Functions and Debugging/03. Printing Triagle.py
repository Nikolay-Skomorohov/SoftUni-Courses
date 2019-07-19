def print_top(number):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()


def print_bottom(number):
    for i in range(number, 1, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()


def main():
    num = abs(int(input()))
    print_top(num)
    print_bottom(num)


if __name__ == '__main__':
    main()
