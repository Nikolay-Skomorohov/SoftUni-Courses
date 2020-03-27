class take_skip:
    def __init__(self, step, count):
        self.count = count
        self.step = step
        self.num = 0
        self.iter_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.count - 1:
            raise StopIteration
        counter = self.iter_count
        self.iter_count += self.step
        self.num += 1
        return counter


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

