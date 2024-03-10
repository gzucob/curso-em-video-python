from utilityCeV import moeda

valor = float(input('Digite um valor: R$ '))
print(f'O valor informado foi R${valor}.')
print(f'Seu dobro é {moeda.dobro(valor, True)}')
print(f'Sua metade é {moeda.metade(valor, True)}')
print(f'Variação de 10% para mais é {moeda.aumentar(valor, 10, True)}')
print(f'Variação de 10% para menos é {moeda.diminuir(valor, 10, True)}')
