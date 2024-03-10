print('CADASTRO DE PESSOAS')
print('=' * 30)
tot18 = htot = mtot20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'F' and sexo not in 'M':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        htot += 1
    if sexo == 'F' and idade < 20:
        mtot20 += 1
    continuar = ' '
    while continuar not in 'S' and continuar not in 'N':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {htot} homens cadastrados.')
print(f'Temos {mtot20} mulheres com menos de 20 anos')
