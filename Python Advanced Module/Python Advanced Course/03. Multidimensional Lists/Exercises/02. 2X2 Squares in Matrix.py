def matrix_input() -> tuple:
    (rows_count, columns_count) = [int(x) for x in input().split(" ")]
    matrix = [[x for x in input().split(" ")] for i in range(rows_count)]
    return tuple([matrix, rows_count, columns_count])


def check_square_symbols(matrix: list, row_len: int, col_len: int) -> int:
    result = 0
    for row in range(0, row_len - 1):
        for col in range(0, col_len - 1):
            if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
                result += 1
    return result


def main():
    matrix = matrix_input()
    print(check_square_symbols(matrix[0], matrix[1], matrix[2]))


if __name__ == "__main__":
    main()
