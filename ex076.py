lista = ('Pão', 10.00,
         'Café', 24.99,
         'Açucar', 19.90,
         'Arroz', 18.99,
         'Azeite', 7.99)
print(f'{"LISTA DE COMPRAS":^40}')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
