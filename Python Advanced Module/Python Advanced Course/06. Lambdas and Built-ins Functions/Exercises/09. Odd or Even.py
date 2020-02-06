command = input()
numbers = [int(x) for x in input().split(" ")]
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
odd_nums = list(filter(lambda x: x % 2 == 1, numbers))
even_sum = sum(list(map(lambda x: x * len(numbers), even_nums)))
odd_sum = sum(list(map(lambda x: x * len(numbers), odd_nums)))

if command == "Odd":
    print(odd_sum)
else:
    print(even_sum)
