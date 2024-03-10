num = (int(input('Informe um número: ')),
       int(input('Informe um número: ')),
       int(input('Informe um número: ')),
       int(input('Informe um número: ')))
print(f'Os valores digitados são: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na posição: {num.index(3)}')
else:
    print('O valor 3 não apareceu nenhuma vez.')
print('Os valores pares digitados foram ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
