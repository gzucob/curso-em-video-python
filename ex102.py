def fatorial(n, show):

    """
    ---Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: mostra o calculo completo (opcional)
    :return: o valor do fatorial de um número n
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


var = int(input('Digite um número: '))
print(fatorial(var, show=True))
