def sum_even_odd(number_string):
    odd_sum = 0
    even_sum = 0

    for char in number_string:
        if int(char) % 2 == 1:
            odd_sum += int(char)
        elif int(char) % 2 == 0:
            even_sum += int(char)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()

print(sum_even_odd(number))
