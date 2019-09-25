from abc import ABC, abstractmethod


class BaseMonster(ABC):
    def __init__(self, name, idt, strength, ugliness):
        self.name = name
        self.idt = idt
        self.strength = int(strength)
        self.ugliness = ugliness

    @abstractmethod
    def do_something(self):
        pass


class Hydralisk(BaseMonster):
    def __init__(self, name, idt, strength, ugliness, range):
        BaseMonster.__init__(self, name, idt, strength, ugliness)
        self.range = range

    def do_something(self):
        pass

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value):
        if value is None:
            print("__init__() missing 1 required positional argument: 'range'")
            raise ValueError
        if str(value).isalpha():
            self.__range = value
        else:
            print("Range must be string")
            raise Exception


class Zergling(BaseMonster):
    def __init__(self, name, idt, strength, ugliness, speed):
        BaseMonster.__init__(self, name, idt, strength, ugliness)
        self.speed = speed

    def do_something(self):
        pass

    @property
    def speed(self):
        return int(self.__speed)

    @speed.setter
    def speed(self, value):
        if value is None:
            print("__init__() missing 1 required positional argument: 'speed'")
            raise ValueError
        try:
            int(value)
            self.__speed = value
        except ValueError:
            print("Speed must be integer")
            raise ValueError


monsters_list = []
while True:
    command = input()
    if command == "stopAddingArmy":
        break
    else:
        try:
            new_object = eval(command)
            monsters_list.append(new_object)
        except TypeError as text:
            if "BaseMonster" in command:
                print("Can't instantiate abstract class BaseMonster with abstract methods __init__")
            else:
                print(text)
        except:
            continue


overall_speed = sum(x.speed for x in monsters_list if isinstance(x, Zergling))
overall_strength = sum(x.strength for x in monsters_list)
count_zerg = sum(1 for x in monsters_list if isinstance(x, Zergling))
count_hydra = sum(1 for x in monsters_list if isinstance(x, Hydralisk))
print(f"Overall speed of army: {overall_speed}")
print(f"Overall stength: {overall_strength}")
print(f"Hydralisk: {count_hydra}; Zergling: {count_zerg}")
