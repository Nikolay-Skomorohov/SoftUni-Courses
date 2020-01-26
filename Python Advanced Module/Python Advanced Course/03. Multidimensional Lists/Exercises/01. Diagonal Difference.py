def matrix_input():
    number = int(input())
    matrix = [[int(x) for x in input().split(" ")] for i in range(number)]
    return matrix


def prime_diagonal_sum(matrix: list):
    prime_sum = 0
    for i in range(len(matrix)):
        prime_sum += matrix[i][i]
    return prime_sum


def second_diagonal_sum(matrix: list):
    second_sum = 0
    for i in range(len(matrix)):
        second_sum += matrix[0 + i][(len(matrix) - 1) - i]
    return second_sum


def main():
    matrix = matrix_input()
    print(f"{abs(prime_diagonal_sum(matrix) - second_diagonal_sum(matrix))}")


if __name__ == "__main__":
    main()
