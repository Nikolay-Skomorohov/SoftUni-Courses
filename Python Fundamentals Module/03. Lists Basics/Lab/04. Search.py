n = int(input())
word = input()

input_list = []

for i in range(n):
    input_list.append(input())

result_list = []

for item in input_list:
    if word in item:
        result_list.append(item)

print(input_list)
print(result_list)