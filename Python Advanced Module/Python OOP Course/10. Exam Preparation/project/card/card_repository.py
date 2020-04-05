from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if any(x.name == card.name for x in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        self.cards.remove([x for x in self.cards if x.name == card][0])
        self.count -= 1

    def find(self, name: str):
        result = [x for x in self.cards if x.name == name][0]
        return result
