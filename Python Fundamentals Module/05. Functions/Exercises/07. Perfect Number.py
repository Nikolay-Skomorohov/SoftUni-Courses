def check_number(num: int):
    result = []
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 = sum1 + i
            result.append(i)



number = int(input())
