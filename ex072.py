cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
        'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
        'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0:
        print('Tente novamente.')
        num = int(input('Digite um número entre 0 e 20: '))
    else:
        print(cont[num])
    continuar = ' '
    while continuar not in 'S' and continuar not in 'N':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Processo Finalizado!')
