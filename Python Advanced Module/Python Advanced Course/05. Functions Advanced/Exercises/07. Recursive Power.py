def recursive_power(num, power):
    result = 1
    if power == 0:
        return result
    else:
        result *= num
        return result * recursive_power(num, power - 1)
