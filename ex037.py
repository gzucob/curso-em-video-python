print('conversor de bases numericas'.upper())
var = int(input('Digite um numero: '))
print('''Escolha uma das bases numericas:
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opcao = int(input('Qual a sua opcao? '))
if opcao == 1:
    print(f'O valor {var} em BINARIO e {bin(var)[2:]}')
elif opcao == 2:
    print(f'O valor {var} em OCTAL e {oct(var)[2:]}')
elif opcao == 3:
    print(f'O valor {var} em HEXADECIMAL e {hex(var)[2:]}')
else:
    print('opcao invalida'.upper())
