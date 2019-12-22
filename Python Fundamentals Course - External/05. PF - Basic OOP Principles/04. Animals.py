from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def produce_sound(self):
        return "What does the fox say?"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise Exception("Invalid input!")
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value == "" or value < 0:
            raise Exception("Invalid input!")
        else:
            self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value == "":
            raise Exception("Invalid input!")
        else:
            self.__gender = value

    def __str__(self):
        return f"{self.__class__.__name__}\n" \
               f"{self.name} {self.age} {self.gender}\n" \
               f"{self.produce_sound()}"


class Dog(Animal):
    def produce_sound(self):
        return "Woof!"


class Frog(Animal):
    def produce_sound(self):
        return "Ribbit"


class Cat(Animal):
    def produce_sound(self):
        return "Meow meow"


class Kitten(Cat):
    def produce_sound(self):
        return "Meow"

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = "Female"


class Tomcat(Cat):
    def produce_sound(self):
        return "MEOW"

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = "Male"


def main():
    animal_type_input = input()
    animal_specs_input = input().split()
    while animal_type_input != "Beast!":
        try:
            if animal_type_input == "Dog":
                animal_to_create = Dog(animal_specs_input[0],
                                       int(animal_specs_input[1]),
                                       animal_specs_input[2])

            elif animal_type_input == "Frog":
                animal_to_create = Frog(animal_specs_input[0],
                                        int(animal_specs_input[1]),
                                        animal_specs_input[2])

            elif animal_type_input == "Cat":
                animal_to_create = Cat(animal_specs_input[0],
                                       int(animal_specs_input[1]),
                                       animal_specs_input[2])

            elif animal_type_input == "Kitten":
                animal_to_create = Kitten(animal_specs_input[0],
                                          int(animal_specs_input[1]),
                                          animal_specs_input[2])

            elif animal_type_input == "Tomcat":
                animal_to_create = Tomcat(animal_specs_input[0],
                                          int(animal_specs_input[1]),
                                          animal_specs_input[2])
            else:
                raise Exception("Invalid input!")
            print(animal_to_create)
        except Exception as text:
            print(text)

        animal_type_input = input()
        if animal_type_input == "Beast!":
            break
        animal_specs_input = input().split()


if __name__ == "__main__":
    main()
