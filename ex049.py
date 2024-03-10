from random import randint
vitorias = 0
escolha = 0

while True:
    while escolha == 1 or escolha == 2:
        escolha = str(input('Par[1]\nImpar[2]\n')).strip()[0]
        if escolha != 1 or escolha != 2:
            print('opção inválida'.upper())

    jogador = int(input('Digite um número: '))
    pc = randint(0, 10)
    total = jogador + pc

    print(f'Você jogou {jogador} o computador jogou {pc}, totalizando {total}.')
    print('deu par'.upper()if total % 2 == 0 else 'deu impar'.upper())

    if escolha == 1:
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break

    elif escolha == 2:
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break

    print('Vamos jogar novamente...')
print(f'Jogo encerrado! Você ganhou {vitorias} vezes.')