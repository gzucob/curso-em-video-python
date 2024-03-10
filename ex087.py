matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = st3 = sc2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
for l in range(0, 3):
    st3 += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        sc2 = matriz[1][c]
    elif matriz[1][c] > sc2:
        sc2 = matriz[1][c]
print(f'A soma dos números pares é {par}')
print(f'A soma dos números na terceira coluna é {st3}')
print(f'O maior valor da linha três é {sc2}')