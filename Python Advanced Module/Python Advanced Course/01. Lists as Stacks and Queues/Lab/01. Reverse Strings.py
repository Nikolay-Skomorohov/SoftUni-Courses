def stack_task(input_string: str):
    text = list(input_string)
    result = []
    for i in range(len(input_string)):
        result.append(text.pop())
    return "".join(result)


print(stack_task(input()))
