def function():
    number = int(input())
    names_set = set([input() for name in range(number)])
    return names_set


result = function()

[print(x) for x in result]

