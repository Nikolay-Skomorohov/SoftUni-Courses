from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if any(x.username == player.username for x in self.players):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        self.players.remove([x for x in self.players if x.username == player][0])
        self.count -= 1

    def find(self, username: str):
        result = [x for x in self.players if x.username == username][0]
        return result
