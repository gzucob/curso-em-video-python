r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print(f'Os segmento {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triangulo EQUILÁTERO.')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print(f'Os segmento {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triangulo ISÓCELES.')
    elif r1 != r2 != r3:
        print(f'Os segmento {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triangulo ESCALENO.')
else:
    print('Os segmentos acima não podem formar um triangulo.')

