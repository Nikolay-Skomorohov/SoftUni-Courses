def function():
    text = input()
    result = {}
    for char in text:
        if char in result.keys():
            result[char] += 1
        else:
            result[char] = 1
    return result


to_print = function()

for key, value in sorted(to_print.items(), key=lambda x: x[0]):
    print(f"{key}: {value} time/s")
