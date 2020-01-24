def function():
    n = int(input())
    result = set()
    for item in range(n):
        temp_list = input().split(" ")
        for element in temp_list:
            result.add(element)
    return result


[print(x) for x in function()]
