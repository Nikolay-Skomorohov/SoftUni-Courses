class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.cards = []


class Card(Person):
    def __init__(self, card_num: int, first_name: str, last_name: str):
        Person.__init__(self, first_name, last_name)
        self.card_num = card_num
        self.valid = None
        self.owner = None

    def check_card_validity(self):
        if sum(int(x) for x in str(self.card_num)) % 7 == 0:
            self.valid = True
        else:
            self.valid = False


class Ticket(Person):
    def __init__(self, ticket_num: int, destination: str, first_name: str, last_name: str, use_card: int):
        Person.__init__(self, first_name, last_name)
        self.ticket_num = ticket_num
        self.destination = destination
        self.use_card = use_card
        self.price = sum(ord(x) for x in self.destination) / 100

    def __str__(self):
        return f"{self.full_name}:\n" \
               f"--{self.destination}: {self.price:.2f}\n" \
               f"--{self.destination}: {self.price / 2:.2f} (using card {self.use_card}"


def print_result(tickets_list: list):
    for ticket in tickets_list:
        print(ticket)


def main():
    people_list = []
    tickets_list = []
    personal_info_num = int(input())
    for dude in range(personal_info_num):
        person = input().split()
        new_person = Person(person[0], person[1])
        new_person.cards.append(person[2])
        people_list.append(new_person)

    while True:
        command = input()
        if command == "time to leave!":
            break
        else:
            new_ticket = input().split()

    print_result(tickets_list)


if __name__ == "__main__":
    main()
