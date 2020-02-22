def get_magic_triangle(n):
    result = [[1], [1, 1]]
    for line in range(2, n):
        new_row = [1]
        for cell in range(1, line):
            num_index = [line, cell - 1]
            new_row.append(result[line - 1][cell] + result[line - 1][cell - 1])
        new_row.append(1)
        result.append(new_row)
    return result


print(get_magic_triangle(7))
