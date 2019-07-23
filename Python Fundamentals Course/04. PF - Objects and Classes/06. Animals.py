class Animal:
    def __init__(self, name, age, par):
        self.name = name
        self.age = age
        self.par = par


class Dog(Animal):
    def talk(self):
        to_print = """I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."""
        return to_print


class Cat(Animal):
    def talk(self):
        to_print = """I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."""
        return to_print


class Snake(Animal):
    def talk(self):
        to_print = """I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."""
        return to_print


def find_animal(name: str, animals_list: list):
    to_speak = ""
    for item in animals_list:
        if item.name == name:
            to_speak = item
    return to_speak


def print_result(animals: list):
    for dog in animals:
        if isinstance(dog, Dog):
            print(f"Dog: {dog.name}"
                  f", Age: {dog.age}"
                  f", Number Of Legs: {dog.par}")
    for cat in animals:
        if isinstance(cat, Cat):
            print(f"Cat: {cat.name}"
                  f", Age: {cat.age}"
                  f", IQ: {cat.par}")
    for snake in animals:
        if isinstance(snake, Snake):
            print(f"Snake: {snake.name}"
                  f", Age: {snake.age}"
                  f", Cruelty: {snake.par}")


def main():
    animals_list = []

    input_list = [item for item in input().split()]

    while input_list[0] != "I'm":
        if input_list[0] == "talk":
            to_speak = find_animal(input_list[1], animals_list)
            print(to_speak.talk())
        elif input_list[0] == "Dog":
            new_animal = Dog(input_list[1], input_list[2], input_list[3])
            animals_list.append(new_animal)
        elif input_list[0] == "Cat":
            new_animal = Cat(input_list[1], input_list[2], input_list[3])
            animals_list.append(new_animal)
        elif input_list[0] == "Snake":
            new_animal = Snake(input_list[1], input_list[2], input_list[3])
            animals_list.append(new_animal)

        input_list = [item for item in input().split()]

    print_result(animals_list)


if __name__ == "__main__":
    main()
