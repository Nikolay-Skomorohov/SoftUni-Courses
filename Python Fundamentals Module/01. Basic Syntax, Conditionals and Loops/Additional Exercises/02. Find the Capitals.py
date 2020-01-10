input_string = list(input())

result = []

for index in range(len(input_string)):
    letter = input_string[index]
    if letter.isupper():
        result.append(index)

print(result)
