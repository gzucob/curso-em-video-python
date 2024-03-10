pi = [[], []]
valor = 0
for val in range(0, 7):
    valor = int(input('Informe um valor: '))
    if valor % 2 == 0:
        pi[0].append(valor)
    else:
        pi[1].append(valor)
pi[0].sort()
print(f'São pares: {pi[0]}')
pi[1].sort()
print(f'São ímpares: {pi[1]}')
