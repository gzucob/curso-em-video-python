def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'{idade} anos, não vota.'
    elif idade >= 16 or idade > 65:
        return f'{idade} anos, voto opcional.'
    elif idade > 18:
        return f'{idade} anos, voto obrigatório.'


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
