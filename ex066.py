sair = 999
s = q = 0
print('Digite "999" para parar.')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'A soma entre os {q} números é igual a {s}')
