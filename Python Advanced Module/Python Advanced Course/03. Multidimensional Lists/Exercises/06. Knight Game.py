def matrix_input() -> tuple:
    removed = 0
    rows_count = int(input())
    matrix = [[x for x in list(input())] for i in range(rows_count)]
    return matrix, rows_count, removed


def remove_knight(inputs: tuple) -> tuple:
    removed = inputs[2]
    knights_dict = inputs[3]
    matrix = inputs[0]
    to_remove = max(knights_dict, key=knights_dict.get)
    matrix[to_remove[0]][to_remove[1]] = "0"
    removed += 1
    return matrix, inputs[1], removed


def check_moves(inputs: tuple) -> tuple:
    removed = inputs[2]
    result = 0
    knights_dict = {}
    matrix = inputs[0]
    rows_count = inputs[1]
    for row in range(len(matrix)):
        for column in range(rows_count):
            if matrix[row][column] == "K":
                knights_dict[tuple([row, column])] = 0
                knight_moves = [(row + 1, column + 2),
                                (row - 1, column + 2),
                                (row + 1, column - 2),
                                (row - 1, column - 2),
                                (row + 2, column + 1),
                                (row + 2, column - 1),
                                (row - 2, column + 1),
                                (row - 2, column - 1),
                                ]
                for move in knight_moves:
                    if (rows_count > move[0] >= 0) and (rows_count > move[1] >= 0):
                        attack1 = matrix[move[0]][move[1]]
                        if attack1 == "K":
                            knights_dict[tuple([row, column])] += 1
                    else:
                        continue
            elif matrix[row][column] == '0':
                continue
    for knight in knights_dict.keys():
        result += knights_dict[knight]
    return matrix, rows_count, removed, knights_dict, result


def main():
    matrix = matrix_input()
    check = check_moves(matrix)
    while check[-1] != 0:
        new = remove_knight(check)
        check = check_moves(new)
    print(check_moves(check)[2])


if __name__ == "__main__":
    main()
