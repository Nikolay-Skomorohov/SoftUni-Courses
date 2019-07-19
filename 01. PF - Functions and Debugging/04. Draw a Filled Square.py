def print_header_footer(num):
    print(f"-" * (num * 2))


def print_body(num):
    stupid = "\\/"
    print(f"-{stupid * num}-")


def main():
    number = int(input())
    print_header_footer(number)
    for i in range(1, number-1):
        print_body(number - 1)
    print_header_footer(number)


if __name__ == '__main__':
    main()
