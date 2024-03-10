from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
game = {"player1": randint(1, 6),
        "player2": randint(1, 6),
        "player3": randint(1, 6),
        "player4": randint(1, 6)}
for k, v in game.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('O VENCEDOR FOI...')
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º colocado foi o {v[0]} com {v[1]}.')
