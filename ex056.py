somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
for p in range(1, 2):
    nome = str(input('Qual o seu nome? ')).capitalize()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Informe seu sexo [M]/[F]: ')).capitalize()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        mulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo e {mediaidade:.2f}.')
print(f'O homem mais velho se chama {nomevelho} tem {maioridadehomem} anos.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')