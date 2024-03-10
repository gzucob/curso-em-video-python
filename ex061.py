var1 = int(input('Informe um número: '))
var2 = int(input('Quer que pule de quanto em quanto? '))
termo = var1
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += var2
    cont += 1
print('Fim')