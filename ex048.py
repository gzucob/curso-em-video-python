soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f'A soma dos {cont} números ímpares múltiplos de 3 é {soma}')

