class Animal:
    def __init__(self, name: str, age: int, par: int):
        self.name = name
        self.age = age
        self.par = par


class Dog(Animal):
    def talk(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."


class Cat(Animal):
    def talk(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."


class Snake(Animal):
    def talk(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."


def find_animal(name: str, animals_list: list):
    to_talk = next(filter(lambda x: x.name == name, animals_list))
    print(to_talk.talk())


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

    while " ".join(input_list) != "I'm your Huckleberry":
        if input_list[0] == "talk":
            find_animal(input_list[1], animals_list)
        elif input_list[0] == "Dog":
            new_animal = Dog(input_list[1], int(input_list[2]), int(input_list[3]))
            animals_list.append(new_animal)
        elif input_list[0] == "Cat":
            new_animal = Cat(input_list[1], int(input_list[2]), int(input_list[3]))
            animals_list.append(new_animal)
        elif input_list[0] == "Snake":
            new_animal = Snake(input_list[1], int(input_list[2]), int(input_list[3]))
            animals_list.append(new_animal)
        input_list = [item for item in input().split()]

    print_result(animals_list)


if __name__ == "__main__":
    main()
