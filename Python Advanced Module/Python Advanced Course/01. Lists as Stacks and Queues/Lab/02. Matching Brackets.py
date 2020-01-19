def solve(input_string: str):
    open_list = []
    for i in range(len(input_string)):
        if input_string[i] == "(":
            open_list.append(i)
        elif input_string[i] == ")":
            print(f"{input_string[open_list.pop():i + 1]}")


input_expression = input()
solve(input_expression)