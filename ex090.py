aluno = dict()
aluno["nome"] = str(input('Nome do aluno: '))
aluno["media"] = float(input(f'Media do {aluno["nome"]}: '))
if aluno["media"] >= 7:
    print('Parabéns! Aprovado.')
elif aluno["media"] >= 5:
    print('Recuperação.')
else:
    print('Reprovado!')
