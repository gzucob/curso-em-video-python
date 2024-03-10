n = total = soma = 0
n = int(input('Digite um número[999 para parar]: '))
while n != 999:
    total += 1
    soma += n
    n = int(input('Digite um número[999 para parar]: '))
print(f'Foram digitados {total} números, e sua soma é {soma}')
