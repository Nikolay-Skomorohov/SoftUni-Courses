numbers_list = [int(x) for x in input().split(", ")]

positives = [str(num) for num in numbers_list if num >= 0]
negative = [str(num) for num in numbers_list if num < 0]
odd = [str(num) for num in numbers_list if num % 2 == 1]
even = [str(num) for num in numbers_list if num % 2 == 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
