from datetime import date
atual = date.today().year
maior = 0
menor = 0
for p in range(1, 8):
    nasc = int(input('Em que ano você nasceu? '))
    idade = atual - nasc
    if idade >= 17:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já possuem maioridade.')
print(f'{menor} pessoas ainda não atingiram a maioridade.')
