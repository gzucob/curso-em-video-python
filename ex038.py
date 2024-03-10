var1 = int(input('Digite um numero: '))
var2 = int(input('Digite um numero: '))
if var1 > var2:
    print(f'O valor {var1} e maior que {var2}.')
elif var2 > var1:
    print(f'O valor {var2} e maior que {var1}.')
elif var1 == var2:
    print(f'Os valores {var1} e {var2} sao iguais.')
