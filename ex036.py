print('Minha casa minha vida'.upper())
casa = float(input('Qual o valor da casa?R$'))
salario = float(input('Qual o seu salario?R$'))
anos = float(input('Em quanto tempo deseja pagar? '))
minimo = salario * 30 / 100
parcelas = casa / (anos * 12)
if parcelas <= minimo:
    print(f'EMPRESTIMO CONCEDIDO\nO valor de cada parcela sera de R${parcelas:.2f}.')
else:
    print('EMPRESTIMO NEGADO')


