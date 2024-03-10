#import random
#distancia = random.randrange(0, 1000)
distancia = int(input('Quantos km tem sua viagem: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O valor da sua viagem é R${preco:.2f}.')

