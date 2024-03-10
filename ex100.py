from random import randint


def sorteio(lista):
    print('Sorteando os valores...')
    print('-' * 30)
    for cont in range(0, 5):        # cont = CONTADOR
        n = randint(0, 10)          # n = NUMERO
        lista.append(n)
        print(f'{n} ', end='')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, temos {soma} ')
    print('Finalizado!')


numeros = list()
sorteio(numeros)
somapar(numeros)
