def print_sign(number):
    if number < 0:
        print(f"The number {number} is negative.")
    elif number == 0:
        print(f"The number {number} is zero.")
    else:
        print(f"The number {number} is positive.")


if __name__ == '__main__':
    print_sign(int(input()))
