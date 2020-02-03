def func_executor(*args):
    result = []
    for function in args:
        if len(function[1]) > 1:
            result.append(function[0](*function[1]))
        else:
            result.append(function[0](*function[1]))
    return result
