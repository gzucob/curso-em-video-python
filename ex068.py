from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um número: '))
    pc = randint(0, 10)
    total = jogador + pc
    escolha = ' '
    while escolha not in 'P' and escolha not in 'I':
        escolha = str(input('Par[P]\nImpar[I]\nEscolho: ')).strip().upper()[0]
    print(f'Você jogou {jogador} o computador jogou {pc}, totalizando {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Jogo encerrado! Você ganhou {vitorias} vez(es).')
