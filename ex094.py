pessoa = dict()
dados = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa["sexo"] in 'MF':
            break
        print('Erro! Apenas M ou F.')
    pessoa["idade"] = int(input('Idade: '))
    soma += pessoa["idade"]
    dados.append(pessoa.copy())
    while True:
        continuar = str(input('Continuar: [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Apenas S ou N.')
    if continuar == 'N':
        break
print(f'Ao todo foram cadastradas {len(dados)} pessoas.')
media = soma / len(dados)
print(f'A média de idade é {media:5.2f}')
print(f'As mulheres cadastradas foram ', end='')
for p in dados:
    if p["sexo"] in 'F':
        print(f'{p["nome"]}', end='')
print()
print(f'Lista de pessoas com a idade maior que a média: ')
for p in dados:
    if p["idade"] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
