import math
print('>>>TEORAMA DE PITAGORAS<<<')
co = float(input('Valor do Cateto Oposto: '))
ca = float(input('Valor do Cateto Adjacente: '))
h = math.hypot(co, ca)
print(f'O valor da hipotenusa é {h:.2f}')
