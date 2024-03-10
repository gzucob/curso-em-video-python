cont = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print(f'O numero {c} é divisivel por {n}.')
    else:
        print(f'O numero {c} não é divisivel por {n}.')
print(f'O numero {n} foi dividido {cont}x')
if cont == 2:
    print(f'O numero é {n} é primo')
else:
    print(f'O numero não é {n} é primo')
