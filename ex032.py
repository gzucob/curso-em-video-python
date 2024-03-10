print('DESCUBRA SE O ANO BISSEXTO OU NÃO')
ano = int(input('Qual ano você quer saber: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
