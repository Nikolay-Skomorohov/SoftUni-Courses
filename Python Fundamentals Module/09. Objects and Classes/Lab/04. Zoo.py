class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: " \
                      f"{', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: " \
                      f"{', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: " \
                      f"{', '.join(self.birds)}\n"
        result += f"Total animals: {self.__animals}"
        return result


zoo_name = input()
the_zoo = Zoo(zoo_name)
n = int(input())
for line in range(n):
    input_line = input().split(" ")
    the_zoo.add_animal(input_line[0], input_line[1])

to_print = input()
print(the_zoo.get_info(to_print))
