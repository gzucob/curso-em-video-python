palavras = ('saco', 'fome', 'transer', 'jubileu', 'pode5')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
