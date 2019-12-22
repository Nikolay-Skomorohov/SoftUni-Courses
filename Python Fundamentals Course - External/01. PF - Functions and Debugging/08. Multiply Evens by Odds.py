def even_by_odd(number):
    sum_evens = 0
    sum_odds = 0
    for i in number:
        if i == "-":
            continue
        elif int(i) % 2 == 1:
            sum_odds += int(i)
        else:
            sum_evens += int(i)
    return sum_evens * sum_odds


def main():
    num = input()
    print(even_by_odd(num))


if __name__ == "__main__":
    main()
