def solution():
    def integers():
        start = 1
        while True:
            yield start
            start += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in range(n):
            func = next(seq)
            result.append(func)
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
