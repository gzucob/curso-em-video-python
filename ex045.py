import random
import time
print('{:-^20}'.format(' jokenpô ').upper())

print('''suas opções
[0] pedra
[1] papel
[2] tesoura'''.upper())
jogador = int(input('Qual é sua jogada? '))

print('=' * 20)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
time.sleep(1)
print('=' * 20)

jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
print(f'Você escolheu: {jogadas[jogador]}')
pc = random.randint(0, 2)
print(f'O computador escolheu: {jogadas[pc]}')

if pc == 0:  # pc jogou PEDRA
    if jogador == 0:
        print('empate!'.upper())
    elif jogador == 1:
        print('você ganhou!'.upper())
    elif jogador == 2:
        print('você perdeu!'.upper())
    else:
        print('jogada inválida'.upper())

if pc == 1:  # pc jogou PAPEL
    if jogador == 0:
        print('você perdeu!'.upper())
    elif jogador == 1:
        print('empate!'.upper())
    elif jogador == 2:
        print('você ganhou!'.upper())
    else:
        print('jogada inválida'.upper())

if pc == 2:  # pc jogou TESOURA
    if jogador == 0:
        print('você ganhou!'.upper())
    elif jogador == 1:
        print('você perdeu!'.upper())
    elif jogador == 2:
        print('empate!'.upper())
    else:
        print('jogada inválida'.upper())