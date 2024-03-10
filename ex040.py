nota1 = float(input('Primeira nota? '))
nota2 = float(input('Primeira nota? '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'A media final e {media:.2f}.\nPARABENS, APROVADO!')
elif media <= 5:
    print(f'A media final e {media:.2f}.\nREPROVADO')
else:
    print(f'Sua media final e {media:.2f}.\nRECUPERACAO')
