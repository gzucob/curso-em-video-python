def maior(* num):
    cont = maior = 0
    print('Analisando valores informados...')
    print('=' * 50)
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} números.')
    print(f'O maior valor informado foi {maior}.')


maior(3, 9, 10, 56, 90)
maior(100, 983, 100000, 0)
maior(13453, 4324, 4324, 2)
