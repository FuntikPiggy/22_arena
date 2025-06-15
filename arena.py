import time
from random import choices


class Arena:
    """Класс для создания объекта арены сражений"""

    ORANGE = '\033[33m'
    RED = '\033[31m'

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.players = []

    def add_player(self, player):
        if len(self.players) < self.capacity:
            self.players.append(player)

    def choice_two_players(self):
        self.player1, self.player2 = choices(self.players, k=2)

    def make_move(self):
        self.player2.get_defence(self.player1)
        if self.player2.hp_total > 0:
            print(self.ORANGE + f'{self.player1.name} наносит удар {self.player2.name}, но {self.player2.name} устоял!')
        else:
            print(self.RED + f'{self.player1.name} наносит сокрушительный удар {self.player2.name} и выводит его из боя!')
            self.players.remove(self.player2)
        time.sleep(0.3)
