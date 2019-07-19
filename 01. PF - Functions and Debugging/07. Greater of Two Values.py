def greater_value_char():
    value1 = input()
    value2 = input()
    return max(value1, value2)


def greater_value_string():
    value1 = input()
    value2 = input()
    return max(value1, value2)


def greater_value_int():
    value1 = int(input())
    value2 = int(input())
    return max(value1, value2)


def main():
    value_type = input()
    if value_type == "char":
        print(greater_value_char())
    elif value_type == "string":
        print(greater_value_string())
    else:
        print(greater_value_int())


if __name__ == '__main__':
    main()
