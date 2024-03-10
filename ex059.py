n1 = int(input('Primero valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Outros números
    [5] Sair do programa''')
    opcao = int(input('O que deseja fazer? '))
    print('=' * 20)
    if opcao == 1:
        soma = n1 + n2
        print(f'A some entre {n1} + {n2} = {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} = {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior é o primeiro valor: {n1}')
        else:
            print(f'O maior e o segundo valor: {n2}')
    elif opcao == 4:
        print('Informe outros valores')
        n1 = int(input('Primero valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print()
    else:
        print('Opção Inválida.')
print('saindo do programa...')