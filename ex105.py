def notas(*n, situacao=False):

    """
    ---Programa para verificação de notas:
    :param n: uma ou mais notas
    :param situacao: opcional, mostra a situação do aluno
    :return: dicionario com varias informações sobre aluno e turma
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if situacao:
        if r['media'] < 5:
            r['Situação'] = 'REPROVADO'
        elif r['media'] >= 7:
            r['Situação'] = 'APROVADO!'
        else:
            r['Situação'] = 'RECUPERAÇÃO!'
    return r


respostas = notas(5, 6, 7, situacao=True)
print(respostas)
