num = list()
soma = 0
while True:
    num.append(int(input('Informe um valor: ')))
    soma += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
num.sort(reverse=True)
print(num)
print(f'Foram digitados {soma} valores.')
if 5 in num:
    print(f'O número 5 está na posição {len(num)}')
else:
    print('Não temos 5 nos valores informados.')

