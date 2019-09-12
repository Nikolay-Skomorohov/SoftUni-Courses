class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.cards = []
        self.tickets = []

    def check_for_card(self, input_number: int):
        if any(x.card_num == input_number for x in self.cards):
            return True
        else:
            return False


class Card:
    def __init__(self, first_name: str, last_name: str, card_num: int):
        self.first_name = first_name
        self.last_name = last_name
        self.card_num = card_num
        self.valid = None
        self.owner = self.first_name + " " + self.last_name


class Ticket:
    def __init__(self, first_name: str, last_name: str, destination: str, card_num: int):
        self.first_name = first_name
        self.last_name = last_name
        self.destination = destination
        self.owner = self.first_name + " " + self.last_name
        self.card_num = card_num
        self.use_card = None
        self.price = sum(ord(x) for x in self.destination) / 100

    def __str__(self):
        if self.use_card is not True:
            return f"{self.owner}:\n" \
               f"--{self.destination}: {self.price:.2f}"
        else:
            return f"{self.owner}:\n" \
                   f"--{self.destination}: {self.price / 2:.2f} (using card {self.use_card}"


def print_result(people_list: list):
    for person in people_list:
        if len(person.tickets) < 0:
            for ticket in person.tickets:
                print(ticket)


def check_card_validity(number: int, people_list: list):
    if sum(int(x) for x in str(number)) % 7 == 0:
        if all(x for x in people_list for card in x.cards if card != number):
            print(f"issuing card {number}")
            return True
        else:
            print(f"card {number} already exists for another passenger!")
            return False
    else:
        print(f"card {number} is not valid!")
        return False


def main():
    people_list = []
    cards_list = []
    tickets_list = []
    card_info_num = int(input())
    for card in range(card_info_num):
        new_info = input().split()
        new_card = Card(new_info[0], new_info[1], int(new_info[2]))
        new_card.valid = True
        cards_list.append(new_card)
        # if not all(x.full_name != (new_info[0] + " " + new_info[1]) for x in people_list):
        new_person = Person(new_info[0], new_info[1])
        people_list.append(new_person)
        new_person.cards.append(new_card)

    while True:
        command = input()
        if command == "time to leave!":
            break
        else:
            command = command.split()
            new_ticket = Ticket(command[1], command[2], command[3], int(command[4]))
            tickets_list.append(new_ticket)
            if any(x for x in people_list for card in x.cards if card == new_ticket.card_num):
                new_ticket.use_card = True
            else:
                if check_card_validity(new_ticket.card_num, people_list):
                    new_ticket.use_card = True

            if new_ticket.owner in [x.full_name for x in people_list]:
                new_owner = next(x for x in people_list if x.full_name == new_ticket.owner)
                new_owner.tickets.append(new_ticket)

    print_result(people_list)


if __name__ == "__main__":
    main()
