def fix_calendar(numbers):
    while True:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        if not swapped:
            break
    return numbers


nums = [4, 5, 3, 1, 2]
print(fix_calendar(nums))
