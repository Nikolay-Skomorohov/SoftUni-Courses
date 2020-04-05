from project.player.player import Player
from project.player.beginner import Beginner


class BattleField:
    def __init__(self):
        pass

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead() or enemy.is_dead():
            raise ValueError("Player is dead!")
        if type(attacker) == Beginner:
            attacker.healt += 40
        if type(enemy) == Beginner:
            enemy.healt += 40
