n = int(input())

lines_list = []
for line in range(n):
    new_line = input()
    lines_list.append(new_line)

number_of_rows = {}

for line_index in range(n):
    for char in lines_list[line_index]:
        number_of_rows[char] = 1
        char_needed = 3
        for row_index in range(line_index + 1, n):
            if (char_needed * char) in lines_list[row_index]:
                char_needed += 2
                number_of_rows[char] += 1

print(lines_list)