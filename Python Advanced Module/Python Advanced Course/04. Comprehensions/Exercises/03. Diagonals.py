number = int(input())

input_list = [[int(x) for x in input().split(", ")] for i in range(number)]

first_diagonal1 = sum([input_list[num][num] for num in range(number)])
second_diagonal2 = sum([input_list[num][(number - 1) - num] for num in range(number)])

first_dia_nums = [input_list[num][num] for num in range(number)]
second_dia_nums = [input_list[num][(number - 1) - num] for num in range(number)]

result = ((first_dia_nums, second_dia_nums), (first_diagonal1, second_diagonal2))

print(f"First diagonal: {', '.join([str(x) for x in result[0][0]])}. Sum: {result[1][0]}")
print(f"Second diagonal: {', '.join([str(x) for x in result[0][1]])}. Sum: {result[1][1]}")
