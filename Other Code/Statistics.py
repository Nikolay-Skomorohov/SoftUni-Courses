'''
Program: stats.py
Author: NSS

Computes the statistical average, median and mode of a set of numbers.

1. Define the functions
       mean
       median
       mode
       main
2. User input for numbers
       list_numbers
3. Function initialization
'''

# Define the functions


def mean(numbers):
    the_sum = 0
    for num in numbers:
        the_sum += num
    return print(f"The average of the numbers is {the_sum / len(numbers)}")


def median(numbers):
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return print(f"The median is {numbers[midpoint]}.")
    else:
        return print(f"The median is {(numbers[midpoint] + numbers[midpoint - 1]) / 2}")


def mode(numbers):
    temp_dict = {}
    for num in numbers:
        if num not in temp_dict:
            temp_dict[num] = 1
        else:
            temp_dict[num] += 1
    return print(f"The mode of the numbers is {max(temp_dict.values())}")


def main():
    user_input = input("Enter the numbers separeted by space: ").split()
    list_numbers = []
    for ch in user_input:
        list_numbers.append(int(ch))
    mean(list_numbers)
    median(list_numbers)
    mode(list_numbers)


# Function initialization


main()
