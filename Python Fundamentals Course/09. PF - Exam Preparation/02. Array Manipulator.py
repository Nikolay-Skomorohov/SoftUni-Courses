def exchange_command(integers_list: list, index: int):
    try:
        if index > len(integers_list) or len(integers_list) == 1:
            raise IndexError
        first_half = integers_list[:index + 1]
        second_half = integers_list[index + 1:]
        second_half.extend(first_half)
        return second_half
    except IndexError:
        print('Invalid index')
        return integers_list


def max_command(integers_list: list, even_odd: str):
    if even_odd == "even":
        try:
            evens_list = list(filter(lambda x: x % 2 == 0, integers_list))
            max_even = max(evens_list)
            max_even = integers_list.index(max_even)
            print(max_even)
        except ValueError:
            print("No matches")
    else:
        try:
            odds_list = list(filter(lambda x: x % 2 == 1, integers_list))
            max_odd = max(odds_list)
            max_odd = integers_list.index(max_odd)
            print(max_odd)
        except ValueError:
            print('No matches')


def min_command(integers_list: list, even_odd: str):
    if even_odd == "even":
        try:
            evens_list = list(filter(lambda x: x % 2 == 0, integers_list))
            min_even = min(evens_list)
            min_even = integers_list.index(min_even)
            print(min_even)
        except ValueError:
            print('No matches')
    else:
        try:
            odds_list = list(filter(lambda x: x % 2 == 1, integers_list))
            min_odd = min(odds_list)
            min_odd = integers_list.index(min_odd)
            print(min_odd)
        except ValueError:
            print('No matches')


def first_command(integers_list: list, count: int, even_odd: str):
    if count > len(integers_list):
        return print("Invalid count")
    if even_odd == "even":
        first_indexes = [x for x in integers_list if x % 2 == 0]
        if not first_indexes:
            return print("[]")
        elif len(first_indexes) < count:
            print(first_indexes)
        else:
            return print(first_indexes[:count])
    else:
        first_indexes = [x for x in integers_list if x % 2 == 1][:count]
        if not first_indexes:
            return print("[]")
        elif len(first_indexes) < count:
            print(first_indexes)
        else:
            return print(first_indexes[:count])


def last_command(integers_list: list, count: int, even_odd: str):
    if count > len(integers_list):
        return print("Invalid count")
    if even_odd == "even":
        last_indexes = [x for x in integers_list if x % 2 == 0]
        if not last_indexes:
            return print("[]")
        elif len(last_indexes) < count:
            print(last_indexes)
        else:
            return print(last_indexes[:count])
    else:
        last_indexes = [x for x in integers_list if x % 2 == 1][:count]
        if not last_indexes:
            return print("[]")
        elif len(last_indexes) < count:
            print(last_indexes)
        else:
            to_print = []
            for count_index in range(1, count + 1):
                to_print.append(last_indexes[-count_index])
            return print(to_print)


def main():
    integers_list = [int(x) for x in input().split()]

    while True:
        command = input().split()

        if command[0] == 'exchange':
            integers_list = exchange_command(integers_list, int(command[1]))
        elif command[0] == 'max':
            max_command(integers_list, command[1])
        elif command[0] == 'min':
            min_command(integers_list, command[1])
        elif command[0] == 'first':
            first_command(integers_list, int(command[1]), command[2])
        elif command[0] == 'last':
            last_command(integers_list, int(command[1]), command[2])
        elif command[0] == 'end':
            print(integers_list)
            exit()


if __name__ == "__main__":
    main()
