from datetime import date
atual = date.today().year
nasc = int(input('Em que ano voce nasceu? '))
idade = atual - nasc
print(f'Voce nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('alistamento imediato!'.upper())
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento.\nSeu alistamento sera em {ano}.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Seu alistamento foi ha {saldo} anos.\nSeu alistamento foi em {ano}.')

