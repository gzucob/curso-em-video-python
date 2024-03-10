print('{:=^40}'.format(' LOJA DO ZUCO '))
preco = float(input('Qual o valor do produto? R$'))
print('''FORMAS DE PAGAMENTO:
[1] Dinheiro ou Débito
[2] À vista no crédito
[3] Até 3x no crédito 
[4] 4x ou mais''')
opcao = int(input('Qual a forma desejada? '))
if opcao == 1:
    p1 = preco - (preco * 10 / 100)
    print(f'Essa forma de pagamento tem 10% de desconto, totalizando R${p1:.2f}')
elif opcao == 2:
    p2 = preco - (preco * 5 / 100)
    print(f'Essa forma de pagamento tem 5% de desconto, totalizando R${p2:.2f}')
elif opcao == 3:
    parcela = preco / 3
    print(f'3x de R${parcela:.2f}, fechando os {preco:.2f}')
elif opcao == 4:
    totparc = int(input('Quantas parcelas? '))
    p4 = preco + (preco * 20 / 100)
    parcela = preco / totparc
    print(f'{totparc}x de R${parcela:.2f} totalizando {p4:.2f}, essa forma de pagamento tem 20% de juros.')
else:
    print('OPÇÃO INVÁLIDA')
