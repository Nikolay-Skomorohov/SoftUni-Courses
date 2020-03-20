class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f"{self.username} of type Hero has level {self.level}"


class Elf(Hero):
    def __repr__(self):
        return f"{self.username} of type Elf has level {self.level}"


class MuseElf(Elf):
    def __repr__(self):
        return f"{self.username} of type MuseElf has level {self.level}"


class Wizard(Hero):
    def __repr__(self):
        return f"{self.username} of type Wizard has level {self.level}"


class DarkWizard(Wizard):
    def __repr__(self):
        return f"{self.username} of type DarkWizard has level {self.level}"


class SoulMaster(DarkWizard):
    def __repr__(self):
        return f"{self.username} of type SoulMaster has level {self.level}"


class Knight(Hero):
    def __repr__(self):
        return f"{self.username} of type Knight has level {self.level}"


class DarkKnight(Knight):
    def __repr__(self):
        return f"{self.username} of type DarkKnight has level {self.level}"


class BladeKnight(DarkKnight):
    def __repr__(self):
        return f"{self.username} of type BladeKnight has level {self.level}"