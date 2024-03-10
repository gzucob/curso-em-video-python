salario = float(input('Qual o salário do funcionario?R$ '))
var1 = salario + (salario * 15 / 100)
var2 = salario + (salario * 10 / 100)
if salario <= 1250:
    print(f'O salario aumentou para R${var1:.2f}.')
else:
    print(f'O salario aumentou para R${var2:.2f}.')
