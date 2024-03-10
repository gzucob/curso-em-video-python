nome = dict()
partidas = list()
nome["jogador"] = str(input('Nome do Jogador: '))
matches = int(input(f'Quantas partidas o {nome["jogador"]} jogou: '))
for g in range(1, matches+1):
    partidas.append(int(input(f'Quantos gols marcou na {g}ª partida: ')))
nome["gols"] = partidas[:]
nome["totgol"] = sum(partidas)
print(f'{nome}{nome["gols"]}{nome["totgol"]}')