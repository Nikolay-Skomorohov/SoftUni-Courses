from abc import ABC


class Monster(ABC):
    def __init__(self, name: str, idt: int, strength: int, ugliness: int):
        self.name = name
        self.idt = idt
        self.strength = strength
        self.ugliness = ugliness


class Hydralisk(Monster):
    pass


class Zergling(Monster):
    pass


