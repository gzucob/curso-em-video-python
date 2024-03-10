print('ÍNDICE DE MASSA CORPORAL')
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.2f}')
if imc <= 18.5:
    print('abaixo do peso!'.upper())
elif imc <= 25:
    print('peso ideal'.upper())
elif imc <= 30:
    print('sobrepeso'.upper())
elif imc <= 40:
    print('obesidade'.upper())
else:
    print('obesidade morbida'.upper())
    