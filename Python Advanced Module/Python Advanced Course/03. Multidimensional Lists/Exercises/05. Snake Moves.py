def create_matrix() -> tuple:
    row_count, col_count = [int(x) for x in input().split(" ")]
    matrix = [[" "] for x in range(row_count)]
    for index in range(row_count):
        for num in range(col_count - 1):
            matrix[index].append(" ")
    snake_string = input()
    return matrix, row_count, col_count, snake_string


def snake_moves(inputs: tuple):
    matrix = inputs[0]
    count = 0
    while count != (inputs[1] * inputs[2]):
        snake_string = list(inputs[3][::-1])
        for line in range(1, inputs[1] + 1):
            if line % 2 == 1:
                for index in range(inputs[2]):
                    if matrix[line - 1][index] != " ":
                        continue
                    elif snake_string:
                        matrix[line - 1][index] = snake_string.pop()
                        count += 1
                    else:
                        snake_string = list(inputs[3][::-1])
                        matrix[line - 1][index] = snake_string.pop()
                        count += 1
            else:
                for index in range(inputs[2] - 1, -1, -1):
                    if matrix[line - 1][index] != " ":
                        continue
                    elif snake_string:
                        matrix[line - 1][index] = snake_string.pop()
                        count += 1
                    else:
                        snake_string = list(inputs[3][::-1])
                        matrix[line - 1][index] = snake_string.pop()
                        count += 1
    return matrix


def to_print(input_matrix: list):
    for line in input_matrix:
        print("".join(line))


def main():
    matrix = create_matrix()
    result = snake_moves(matrix)
    to_print(result)


if __name__ == "__main__":
    main()
