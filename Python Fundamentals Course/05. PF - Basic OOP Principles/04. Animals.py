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
        if value == "":
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
    pass


if __name__ == "__main__":
    main()
