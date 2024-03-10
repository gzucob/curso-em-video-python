num = list()
while True:
    n = int(input('Informe um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já informado...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
num.sort()
print(num)
