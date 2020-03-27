class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dictionary):
            raise StopIteration
        dict_item = self.keys[self.index]
        self.index += 1
        return dict_item, self.dictionary[dict_item]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
