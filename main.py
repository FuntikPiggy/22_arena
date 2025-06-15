import time
from random import choice, randint

from players import Warrior, Paladin
from arena import Arena
from things import Thing

PLAYERS_COUNT = 10
PLAYERS_NAMES = [f'Player{i}'for i in range(1, 21)]
THINGS_NAMES = [
    'Магическое кольцо',
    'Кольчуга',
    'Кольцо всевластия',
    'Сапоги скороходы',
    'Двуручный меч',
    'Шлем теней',
    'Кольцо ярости',
    'Плащ ледяной бури',
    'Перчатки титана',
    'Амулет вечной жизни',
    'Сапоги безмолвия',
    'Пояс кровавого клинка',
    'Наплечники огненного воина',
    'Кристалл разума',
    'Мантия иллюзий',
    'Кинжал ядовитой змеи',
    'Часы остановленного времени',
    'Браслет грома',
    'Маска ночного охотника',
    'Кольчужный жилет берсерка'
]


class PrintColors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[31m'

if __name__ == '__main__':
    arena = Arena()
    for i in range(PLAYERS_COUNT):
        name = choice(PLAYERS_NAMES)
        player = choice([Warrior, Paladin])(name)
        for j in range(1, randint(1, 5)):
            player.set_things(Thing(choice(THINGS_NAMES)))
        player.set_total_skills()
        arena.add_player(player)
        time.sleep(0.3)
        print(PrintColors.BLUE + f'На арену вышел боец {name} с характеристиками...')
    while True:
        arena.choice_two_players()
        arena.make_move()
        if len(arena.players) == 1:
            print(PrintColors.CYAN + 'Битва окончена, победитель определён!')
            break
    print(PrintColors.GREEN + f'Новый чемпион - {arena.players[0].name} !')
