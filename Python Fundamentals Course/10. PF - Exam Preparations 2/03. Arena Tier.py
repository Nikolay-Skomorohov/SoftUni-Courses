class Gladiator:
    def __init__(self, name: str, skill: str, value: int):
        self.name = name
        self.skill = skill
        self.value = value
        self.skill_set = []
        self.total_skill = 0

    def add_skill(self):
        return self.skill_set.append([self.skill, self.value])

    def check_skill(self, input_skill, value):
        if input_skill in [x[0] for x in self.skill_set]:
            for k, v in self.skill_set:
                if k == input_skill:
                    if v < value:
                        self.skill_set[k] = value
        elif input_skill not in self.skill_set:
            self.add_skill()

    def calculate_total_skill(self):
        self.total_skill = 0
        for i in self.skill_set:
            self.total_skill += i[1]


def create_gladiator(gladiators_list: list, name: str, skill: str, value: int):
    if all(x.name != name for x in gladiators_list):
        new_gladiator = Gladiator(name, skill, value)
        new_gladiator.add_skill()
        gladiators_list.append(new_gladiator)
    elif any(x.name == name for x in gladiators_list):
        current_gladiator = next(x for x in gladiators_list if x.name == name)
        current_gladiator.skill = skill
        current_gladiator.value = value
        current_gladiator.check_skill(skill, value)
    return gladiators_list


def print_result(gladiator_list: list):
    for gladiator in gladiator_list:
        if gladiator.total_skill == 0:
            gladiator.calculate_total_skill()
    gladiator_list.sort(key=lambda x: x.total_skill, reverse=True)
    for gladiator in gladiator_list:
        print(f"{gladiator.name}: {gladiator.total_skill} skill")
        for skl in sorted(gladiator.skill_set, key=lambda x: (-x[1], x[0])):
            print(f"- {skl[0]} <!> {skl[1]}")


def battle(gladiator_list: list, first_gladiator: Gladiator, second_gladiator: Gladiator):
    for skill_1 in first_gladiator.skill_set:
        for skill_2 in second_gladiator.skill_set:
            if skill_1[0] == skill_2[0]:
                if first_gladiator.total_skill > second_gladiator.total_skill:
                    gladiator_list.remove(second_gladiator)
                    return gladiator_list
                elif first_gladiator.total_skill < second_gladiator.total_skill:
                    gladiator_list.remove(first_gladiator)
                    return gladiator_list
    return gladiator_list


def main():
    gladiator_list = []
    while True:
        command = input()
        if command == "Ave Cesar":
            break
        else:
            if "->" in command:
                command = command.split(" -> ")
                gladiator_list = create_gladiator(gladiator_list, command[0], command[1], int(command[2]))
            elif " vs " in command:
                command = command.split(" vs ")
                first_gladiator = None
                second_gladiator = None
                if any(x for x in gladiator_list if x.name == command[0]):
                    first_gladiator = next(x for x in gladiator_list if x.name == command[0])
                    first_gladiator.calculate_total_skill()
                if any(x for x in gladiator_list if x.name == command[1]):
                    second_gladiator = next(x for x in gladiator_list if x.name == command[1])
                    second_gladiator.calculate_total_skill()
                if first_gladiator and second_gladiator:
                    gladiator_list = battle(gladiator_list, first_gladiator, second_gladiator)
    print_result(gladiator_list)


if __name__ == "__main__":
    main()
