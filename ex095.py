nome = dict()
partidas = list()
time = list()

while True:
    nome.clear()
    nome["jogador"] = str(input('Nome do Jogador: '))
    matches = int(input(f'Quantas partidas o {nome["jogador"]} jogou: '))
    partidas.clear()

    for g in range(1, matches+1):
        partidas.append(int(input(f'Quantos gols marcou na {g}ª partida: ')))
    nome["gols"] = partidas[:]
    nome["totgol"] = sum(partidas)
    time.append(nome.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Apenas S ou N.')
    if continuar == 'N':
        break

print('-' * 40)
print('cod ', end='')
for i in nome.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não exite jogador com o código {busca}')
    else:
        print(f'FAZENDO BUSCA... {time[busca]["jogador"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f' No jogo {i} fez tanto {g} gols.')
print('-' * 30)
print('Programa finalizado!')
