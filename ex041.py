from datetime import date
nasc = int(input('Qual ano você nasceu? '))
atual = date.today().year
idade = atual - nasc
print(f'Sua idade é {idade} ano(s).')
if idade <= 9:
    print('Sua classficação é MIRIM.')
elif idade <= 14:
    print('Sua classificação é INFANTIL.')
elif idade <= 19:
    print('Sua classficação é JUNIOR.')
elif idade <= 25:
    print('Sua classificação é SÊNIOR.')
else:
    print('Sua classificação é MASTER.')
