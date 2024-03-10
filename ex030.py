#import random
#var = random.randrange(0, 1000000)
var = int(input('Digite um número inteiro aleatorio: '))
resultado = var % 2
if resultado == 0:
    print(f'O número {var} é par.')
else:
    print(f'O número {var} é ímpar.')