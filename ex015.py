print('>>>ALUGUEL DE CARRO<<<')
var1 = float(input('Quantos dias foram utilizados? '))
var2 = float(input('Quantos KM foram percorridos? '))

d = (60 * var1) + (0.15 * var2)
print(f'O valor do aluguel é R${d:.2f}')