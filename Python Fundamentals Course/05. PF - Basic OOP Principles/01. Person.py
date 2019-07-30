class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise Exception("Age must be positive!")
        else:
            self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        else:
            self.__name = name

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Child(Person):
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 15:
            raise Exception("Child's age must be less than 15!")
        if age < 0:
            raise Exception("Age must be positive!")
        else:
            self.__age = age


name_input = input()
age_input = int(input())

try:
    child = Child(name_input, age_input)
    print(child)
except Exception as text:
    print(text)
