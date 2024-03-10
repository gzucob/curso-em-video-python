soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'A soma dos {cont} números pares é {soma}')
