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


def input_data():
    animals_list = []
    animal_type_input = input()
    animal_specs_input = input().split()
    while animal_type_input != "Beast!":
        if animal_type_input == "Dog":
            new_dog = Dog(animal_specs_input[0],
                          int(animal_specs_input[1]),
                          animal_specs_input[2])
            animals_list.append(new_dog)
        elif animal_type_input == "Frog":
            new_frog = Frog(animal_specs_input[0],
                            int(animal_specs_input[1]),
                            animal_specs_input[2])
            animals_list.append(new_frog)
        elif animal_type_input == "Cat":
            new_cat = Frog(animal_specs_input[0],
                           int(animal_specs_input[1]),
                           animal_specs_input[2])
            animals_list.append(new_cat)
        elif animal_type_input == "Kitten":
            new_kitten = Frog(animal_specs_input[0],
                              int(animal_specs_input[1]),
                              animal_specs_input[2])
            animals_list.append(new_kitten)
        elif animal_type_input == "Tomcat":
            new_tomcat = Frog(animal_specs_input[0],
                              int(animal_specs_input[1]),
                              animal_specs_input[2])
            animals_list.append(new_tomcat)
        else:
            raise Exception("Invalid animal type input")

        animal_type_input = input()
        animal_specs_input = input().split()
    return animals_list

def print_data():



def main():
    to_print_list = input_data()
    print_data(to_print_list)


if __name__ == "__main__":
    main()
