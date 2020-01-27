def matrix_input() -> tuple:
    row_count, col_count = [int(x) for x in input().split()]
    matrix = [[x for x in input().split(" ")] for i in range(row_count)]
    return matrix, row_count, col_count


def print_matrix(matrix: list):
    [print(*x)for x in matrix]


def receive_commands(inputs: tuple):
    while True:
        command = input().split(" ")
        if command[0] == "END":
            break
        else:
            if command[0] != "swap":
                print("Invalid input!")
                continue
            if len(command) != 5:
                print("Invalid input!")
                continue
            if int(command[1]) in range(0, inputs[1] + 1) \
                    and int(command[3]) in range(0, inputs[1] + 1) \
                    and int(command[2]) in range(0, inputs[2] + 1) \
                    and int(command[4]) in range(0, inputs[2] + 1):
                pass
            else:
                print("Invalid input!")
                continue

        first = inputs[0][int(command[1])][int(command[2])]
        second = inputs[0][int(command[3])][int(command[4])]
        inputs[0][int(command[1])][int(command[2])] = second
        inputs[0][int(command[3])][int(command[4])] = first
        print_matrix(inputs[0])



def main():
    matrix = matrix_input()
    receive_commands(matrix)


if __name__ == "__main__":
    main()
