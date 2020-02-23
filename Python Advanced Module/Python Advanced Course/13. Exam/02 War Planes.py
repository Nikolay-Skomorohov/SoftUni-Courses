def inputs_func() -> tuple:
    matrix_size = int(input())
    matrix = [[x for x in input().split(" ")] for y in range(matrix_size)]
    return matrix_size, matrix


def find_plane(matrix: list) -> list:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "p":
                return [row, col]


def check_field(matrix: list) -> bool:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "t":
                return True
    return False


def perform_move(position: list, direction: str, step: int, matrix: list) -> tuple:
    new_matrix = matrix
    row = position[0]
    col = position[1]
    new_position = None
    try:
        if direction == "up":
            new_position = [row - step, col]
        elif direction == "down":
            new_position = [row + step, col]
        elif direction == "left":
            new_position = [row, col - step]
        elif direction == "right":
            new_position = [row, col + step]
        if new_matrix[new_position[0]][new_position[1]] == ".":
            return True, new_position
    except IndexError:
        pass
    return False, position


def perform_shoot(position: list, direction: str, step: int, matrix: list, destroyed: int) -> tuple:
    new_matrix = matrix
    new_destroyed = destroyed
    row = position[0]
    col = position[1]
    target_position = None
    try:
        if direction == "up":
            target_position = [row - step, col]
        elif direction == "down":
            target_position = [row + step, col]
        elif direction == "left":
            target_position = [row, col - step]
        elif direction == "right":
            target_position = [row, col + step]
        test = new_matrix[target_position[0]][target_position[1]]
        if test == "t":
            new_destroyed += 1
            new_matrix[target_position[0]][target_position[1]] = "x"
        elif test == ".":
            new_matrix[target_position[0]][target_position[1]] = "x"
        elif test == "x":
            pass
    except IndexError:
        pass
    return new_matrix, new_destroyed


def print_result(matrix: list, destroyed: int):
    targets_left = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "t":
                targets_left += 1
    if targets_left == 0:
        print(f"Mission accomplished! All {destroyed} targets destroyed.")
    elif targets_left > 0:
        print(f"Mission failed! {targets_left} targets left.")
    for row in matrix:
        print(f"{' '.join(list(map(str, row)))}")


def main():
    destroyed = 0
    matrix_size, matrix = inputs_func()
    plane_position = find_plane(matrix)
    commands_count = int(input())
    for i in range(commands_count):
        command = input().split(" ")
        if command[0] == "move":
            to_move, position = perform_move(plane_position, command[1], int(command[2]), matrix)
            if to_move:
                matrix[plane_position[0]][plane_position[1]] = "."
                matrix[position[0]][position[1]] = "p"
                plane_position = [position[0], position[1]]
            else:
                pass
        elif command[0] == "shoot":
            result = perform_shoot(plane_position, command[1], int(command[2]), matrix, destroyed)
            destroyed = result[1]
            matrix = result[0]
        if check_field(matrix):
            pass
        else:
            break
    print_result(matrix, destroyed)


if __name__ == '__main__':
    main()

