def matrix_input() -> tuple:
    row_count, column_count = [int(x) for x in input().split(" ")]
    # matrix = [[int(x) for x in input().split(" ")] for i in range(row_count)]
    matrix = []
    for row in range(row_count):
        input_list = list(map(int, input().split()))
        matrix.append(input_list)
    return tuple([matrix, row_count, column_count])


def find_max_sum_square(inputs: tuple) -> tuple:
    result = (None, None)
    for row_count in range(inputs[1] - 2):
        for col_count in range(inputs[2] - 2):
            current_square = [inputs[0][row_count][col_count],
                              inputs[0][row_count][col_count + 1],
                              inputs[0][row_count][col_count + 2],
                              inputs[0][row_count + 1][col_count],
                              inputs[0][row_count + 1][col_count + 1],
                              inputs[0][row_count + 1][col_count + 2],
                              inputs[0][row_count + 2][col_count],
                              inputs[0][row_count + 2][col_count + 1],
                              inputs[0][row_count + 2][col_count + 2],
                              ]
            current_square_sum = sum(current_square)
            if result[0] is not None and result[0] < current_square_sum:
                result = (current_square_sum, current_square)
            elif not result[0]:
                result = (current_square_sum, current_square)
    return result


def to_print(inputs: tuple):
    print(f"Sum = {inputs[0]}")
    for i in range(1, (len(inputs[1]) + 1)):
        if i % 3 == 0:
            print(f"{inputs[1][i - 1]}")
        else:
            print(f"{inputs[1][i - 1]}", end=" ")


def main():
    matrix = matrix_input()
    result = find_max_sum_square(matrix)
    to_print(result)


if __name__ == "__main__":
    main()
