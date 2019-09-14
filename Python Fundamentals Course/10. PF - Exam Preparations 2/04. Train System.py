class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.personal_cards = []
        self.personal_tickets = []
        self.total_tickets_cost = 0

    def calculate_total_cost(self):
        for ticket in self.personal_tickets:
            if ticket.uses_valid_card:
                self.total_tickets_cost += (ticket.ticket_price / 2)
            else:
                self.total_tickets_cost += ticket.ticket_price


class Card:
    def __init__(self, first_name: str, last_name: str, card_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.card_number = card_number


class Ticket:
    def __init__(self, first_name: str, last_name: str, destination: str, card_number_input: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.destination = destination
        self.card_number_input = card_number_input
        self.uses_valid_card = False
        self.ticket_price = sum(ord(x) for x in self.destination) / 100

    def __str__(self):
        if self.uses_valid_card:
            print(f"--{self.destination}: {self.ticket_price / 2:.2f}lv (using card {self.card_number_input})")
        else:
            print(f"--{self.destination}: {self.ticket_price:.2f}lv")


def create_new_person(first_name: str, last_name: str):
    return Person(first_name, last_name)


def create_new_card(first_name: str, last_name: str, card_number: str):
    return Card(first_name, last_name, card_number)


def create_new_ticket(first_name: str, last_name: str, destination: str, card_number_input: str):
    return Ticket(first_name, last_name, destination, card_number_input)


def check_card_info(persons_list: list, card_to_check: str, owner_to_check: str, new_ticket: Ticket):
    person = next(x for x in persons_list if x.full_name == owner_to_check)
    if card_to_check in [x.full_name for x in person.personal_cards]:
        new_ticket.uses_valid_card = True
    else:
        if sum(int(x) for x in card_to_check) % 7 == 0:
            if card_to_check in [x for x in persons_list for card in x.personal_cards if x.full_name != owner_to_check]:
                print(f"card {card_to_check} already exists for another passenger!")
            else:
                new_ticket.uses_valid_card = True
                print(f"issuing card {card_to_check}")
        else:
            print(f"card {card_to_check} is not valid!")


def initial_cards_input():
    persons_list = []
    number_of_cards = int(input())
    for card in range(number_of_cards):
        new_info = input().split()
        new_person = create_new_person(new_info[0], new_info[1])
        new_card = create_new_card(new_info[0], new_info[1], new_info[2])
        new_person.personal_cards.append(new_card)
        persons_list.append(new_person)
    return persons_list


def input_for_tickets(persons_list: list):
    while True:
        input_info = input().split()
        if input_info[0] == "time":
            break
        else:
            new_ticket = create_new_ticket(input_info[1], input_info[2], input_info[3], input_info[4])
            if any(x for x in persons_list if x.full_name == new_ticket.full_name):
                existing_person = next(x for x in persons_list if x.full_name == new_ticket.full_name)
                existing_person.personal_tickets.append(new_ticket)
            else:
                new_person = create_new_person(input_info[1], input_info[2])
                persons_list.append(new_person)
                new_person.personal_tickets.append(new_ticket)

            card_to_check = input_info[4]
            owner_to_check = input_info[1] + " " + input_info[2]
            check_card_info(persons_list, card_to_check, owner_to_check, new_ticket)

    return persons_list


def print_result(persons_list: list):
    for person in persons_list:
        person.calculate_total_cost()
    for person in sorted(persons_list, key=lambda x: -x.total_tickets_cost):
        print(f"{person.full_name}:")
        for ticket in sorted(person.personal_tickets, key=lambda x: -x.ticket_price):
            print(ticket)


def main():
    persons_list = input_for_tickets(initial_cards_input())
    print_result(persons_list)


if __name__ == "__main__":
    main()
