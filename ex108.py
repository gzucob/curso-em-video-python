from utilityCeV import moeda

valor = float(input('Digite um valor: R$ '))
print(f'O valor informado foi R${valor}.')
print(f'Seu dobro é {moeda.virg(moeda.dobro(valor))}')
print(f'Sua metade é {moeda.virg(moeda.metade(valor))}')
print(f'Variação de 10% para mais é {moeda.virg(moeda.aumentar(valor, 10))}')
print(f'Variação de 10% para menos é {moeda.virg(moeda.diminuir(valor, 10))}')
