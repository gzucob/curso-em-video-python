from time import sleep


def contador(i, f, p):      # i = inicio/f = fim/p = passo
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p}')

    if i < f:
        cont = i            # cont = CONTADOR
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Pular de quanto em quanto: '))
contador(inicio, fim, passo)
print('Fim!')
