var1 = int(input('Diga um número qualquer: '))
var2 = int(input('Diga um número qualquer: '))
var3 = int(input('Diga um número qualquer: '))
#variavel menor
if var1 < var2 and var1 < var3:
    menor = var1
if var2 < var1 and var2 < var3:
    menor = var2
if var3 < var1 and var3 < var2:
    menor = var3
#variavel maior
if var1 > var2 and var1 > var3:
    maior = var1
if var2 > var1 and var2 > var3:
    maior = var2
if var3 > var1 and var3 > var2:
    maior = var3
    print(f'O menor valor digitado foi {menor}.\nO maior valor digitado foi {maior}.')
