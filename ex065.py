resp = 'S'
soma = quant = media = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Você quer continuar?[S/N]')).capitalize()[0].strip()
media = soma / quant
print(f'Você digitou {quant} números e média foi {media:.2f}')
print(f'O maior número é {maior} e o menor é {menor}.')
