var1 = int(input('Informe um número: '))
var2 = int(input('Quer que pule de quanto em quanto? '))
termo = var1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += var2
        cont += 1
    print('pausa'.upper())
    mais = int(input('Quantos termos você quer a mais: '))
print(f'Progressão finalizada. Total de termos: {total}')
