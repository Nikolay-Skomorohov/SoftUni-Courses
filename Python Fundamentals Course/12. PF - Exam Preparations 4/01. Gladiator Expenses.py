def calculate_result():
    result = 0
    lost_fights = int(input())
    helmet_price = float(input())
    sword_price = float(input())
    shield_price = float(input())
    armor_price = float(input())

    for fight in range(1, lost_fights + 1):
        if fight % 2 == 0:
            result += helmet_price
        if fight % 3 == 0:
            result += sword_price
        if fight % 2 == 0 and fight % 3 == 0:
            result += shield_price
        if fight % 12 == 0:
            result += armor_price
    return result


def print_result(result: float):
    print(f"Gladiator expenses: {result:.2f} aureus")


def main():
    to_print = calculate_result()
    print_result(to_print)


if __name__ == "__main__":
    main()
