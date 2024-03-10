def numint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('ERRO! Apenas números')
        if ok:
            break
    return valor


num = numint('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')
