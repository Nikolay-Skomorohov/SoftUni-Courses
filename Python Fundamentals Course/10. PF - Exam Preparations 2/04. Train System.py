from abc import ABC


class Person(ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name


class Card(Person):
    def __init__(self, card_num: int, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.card_num = card_num


class Ticket(Person):
    def __init__(self, ticket_num: int, destination: str, first_name: str, last_name: str):
        Person.__init__(self, first_name, last_name)
        self.ticket_num = ticket_num
        self.destination = destination


def main():
    cards_list = []
    cards_number = int(input())
    for card in range(cards_number):
        new_card = input().split()
        cards_list.append(Card(*new_card))

    while True:
        command = input()
        if command == "time to leave!":
            break
        else:
            eval(command)


if __name__ == "__main__":
    main()
