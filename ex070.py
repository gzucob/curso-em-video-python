print('LOJA SUPER BARATÃO!')
print('=' * 30)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
        if cont == 1 or preco < menor:
            menor = preco
            barato = produto
    continuar = ' '
    while continuar not in 'S' and continuar not in 'N':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O valor total gasto foi {total:.2f}')
print(f'Temos {totmil} custando mais de R$1000,00')
print(f'O produto mais barato é {barato} custando R${menor:.2f}')
