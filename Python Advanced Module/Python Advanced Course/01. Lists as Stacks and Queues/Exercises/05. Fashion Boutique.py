def solve():
    seq_ints = [int(x) for x in input().split(" ")]
    capacity = int(input())
    result = 1
    sum_clothes = 0
    while seq_ints:
        item = seq_ints.pop()
        if (sum_clothes + item) < capacity:
            sum_clothes += item
        elif (sum_clothes + item) == capacity and seq_ints:
            result += 1
            sum_clothes = 0
        elif (sum_clothes + item) > capacity:
            result += 1
            sum_clothes = 0
            seq_ints.append(item)

    return result


print(solve())
