cadastro = list()
peso = list()
while True:
    cadastro.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(cadastro)} pessoas.')
print(f'A pessoa com o maior peso é {max(peso)}kg')
print(f'A pessoa com o menor peso é {min(peso)}kg')
