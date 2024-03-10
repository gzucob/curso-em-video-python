from utilityCeV import moeda

valor = float(input('Digite um valor: R$ '))
print(f'O valor informado foi R${valor:.2f}.')
print(f'Seu dobro é R${moeda.dobro(valor):.2f}')
print(f'Sua metade é R${moeda.metade(valor):.2f}')
print(f'Variação de 10% para mais é R${moeda.aumentar(valor, 10):.2f}')
print(f'Variação de 10% para menos é R${moeda.diminuir(valor, 10):.2f}')
