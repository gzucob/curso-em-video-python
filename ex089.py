boletim = list()

while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{"Nº.":<4} {"Nome":<10} {"Media":>10}')
for i, a in enumerate(boletim):
    print(f'{i:<4} {a[0]:<10}  {a[2]:>10.1f}')
