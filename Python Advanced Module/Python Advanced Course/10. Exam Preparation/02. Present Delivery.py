def create_matrix() -> tuple:
    presents_count = int(input())
    neighborhood_size = int(input())
    matrix = [[x for x in input().split(" ")] for y in range(neighborhood_size)]
    return matrix, presents_count, neighborhood_size


def find_santa(matrix: list) -> list:
    position = None
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "S":
                position = [row, col]
    return position


def print_result(santa_position: list, matrix: list, presents_count: int, happy_kids: int):
    matrix[santa_position[0]][santa_position[1]] = "S"
    unhappy_kids = 0
    for row in range(len(matrix)):
        for cell in range(len(matrix[row])):
            if matrix[row][cell] == "V":
                unhappy_kids += 1
    if unhappy_kids > 0 and presents_count == 0:
        print("Santa ran out of presents!")
    for row in range(len(matrix)):
        for cell in range(len(matrix[row])):
            print(f"{matrix[row][cell]}", end=" ")
        print()
    if unhappy_kids == 0:
        print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
    else:
        print(f"No presents for {unhappy_kids} nice kid/s.")


def check_movement(next_position: list, matrix: list, presents_count: int, happy_kids: int):
    row = next_position[0]
    col = next_position[1]
    try:
        if matrix[row][col] == "V":
            presents_count -= 1
            matrix[row][col] = "-"
            happy_kids += 1
        elif matrix[row][col] == "X":
            matrix[row][col] = "-"
        elif matrix[row][col] == "C":
            matrix[row][col] = "-"
            if matrix[row - 1][col] in ("V", "X"):
                if presents_count > 0:
                    presents_count -= 1
                    if matrix[row - 1][col] == "V":
                        happy_kids += 1
                    matrix[row - 1][col] = "-"
                else:
                    return print_result(next_position, matrix, presents_count, happy_kids)
            if matrix[row + 1][col] in ("V", "X"):
                if presents_count > 0:
                    presents_count -= 1
                    if matrix[row + 1][col] == "V":
                        happy_kids += 1
                    matrix[row + 1][col] = "-"
                else:
                    return print_result(next_position, matrix, presents_count, happy_kids)
            if matrix[row][col - 1] in ("V", "X"):
                if presents_count > 0:
                    presents_count -= 1
                    if matrix[row][col - 1] == "V":
                        happy_kids += 1
                    matrix[row][col - 1] = "-"
                else:
                    return print_result(next_position, matrix, presents_count, happy_kids)
            if matrix[row][col + 1] in ("V", "X"):
                if presents_count > 0:
                    presents_count -= 1
                    if matrix[row][col + 1] == "V":
                        happy_kids += 1
                    matrix[row][col + 1] = "-"
                else:
                    return print_result(next_position, matrix, presents_count, happy_kids)
    except IndexError:
        pass
    return next_position, matrix, presents_count, happy_kids


def main():
    happy_kids = 0
    inputs = create_matrix()
    matrix = inputs[0]
    presents_count = inputs[1]
    santa_position = find_santa(matrix)
    next_position = None
    while presents_count > 0:
        command = input()
        if command == "up":
            next_position = [santa_position[0] - 1, santa_position[1]]
        elif command == "down":
            next_position = [santa_position[0] + 1, santa_position[1]]
        elif command == "left":
            next_position = [santa_position[0], santa_position[1] - 1]
        elif command == "right":
            next_position = [santa_position[0], santa_position[1] + 1]
        elif command == "Christmas morning":
            break
        next_position, matrix, presents_count, happy_kids = check_movement(next_position, matrix, presents_count, happy_kids)
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = next_position
        matrix[santa_position[0]][santa_position[1]] = "S"
    print_result(next_position, matrix, presents_count, happy_kids)


if __name__ == '__main__':
    main()
