def inputs():
    initial_string = list(input())
    col_count = int(input())
    matrix = [[x for x in list(input())] for y in range(col_count)]
    return initial_string, col_count, matrix


def find_player(matrix: list):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "P":
                return [row, col]


def check_direction(new_position: list, matrix: list, the_string: list):
    row = new_position[0]
    col = new_position[1]
    new_matrix = matrix
    initial_string = the_string
    move = None
    try:
        if row < 0 or col < 0:
            raise IndexError
        if str(new_matrix[row][col]).isalpha() and str(new_matrix[row][col]) != "P":
            initial_string.append(new_matrix[row][col])
            new_matrix[row][col] = "-"
        else:
            pass
        move = True
    except IndexError:
        if initial_string:
            initial_string.pop()
        move = False
    return move, new_matrix, initial_string


def print_output(final_string: list, matrix: list):
    print(f"{''.join(map(str, final_string))}")
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(f"{matrix[row][col]}", end="")
        print()


def main():
    initial_string, col_count, matrix = inputs()
    player_position = find_player(matrix)
    commands_count = int(input())
    new_direction = []
    for i in range(commands_count):
        direction = input()
        if direction == "up":
            new_direction = [player_position[0] - 1, player_position[1]]
        elif direction == "down":
            new_direction = [player_position[0] + 1, player_position[1]]
        elif direction == "left":
            new_direction = [player_position[0], player_position[1] - 1]
        elif direction == "right":
            new_direction = [player_position[0], player_position[1] + 1]
        perform_check = check_direction(new_direction, matrix, initial_string)
        matrix = perform_check[1]
        initial_string = perform_check[2]
        if perform_check[0]:
            matrix[player_position[0]][player_position[1]] = "-"
            player_position = new_direction
            matrix[player_position[0]][player_position[1]] = "P"
    print_output(initial_string, matrix)


if __name__ == '__main__':
    main()
