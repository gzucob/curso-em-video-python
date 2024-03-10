valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input('Informe um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()
print(valores)
for res in list(valores):
    if res % 2 == 0:
        par.append(res)
        par.sort()
    else:
        impar.append(res)
        impar.sort()
print(f'São pares: {par}')
print(f'São ímpares: {impar}')