while True:
    print('Para sair digite um número negativo.')
    tabuada = int(input('Qual tabuada você quer saber? '))
    if tabuada < 0:
        break
    print('=' * 30)
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('=' * 30)
print('=' * 30)
print('Finalizado!')
