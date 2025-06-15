from random import randint


class Thing:
    def __init__(self, name):
        self.name = name
        self.protection = randint(0, 10)
        self.attack = randint(0, 10)
        self.lives = randint(0, 10)

    def __str__(self):
        return (f'{self.name}: Защита {self.protection}, '
                f'Атака {self.attack}, Жизни {self.lives}')
