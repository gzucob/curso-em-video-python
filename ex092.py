from datetime import datetime
dados = dict()
dados["nome"] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados["idade"] = datetime.now().year - nasc
dados["ctps"] = int(input('Cateira de Trabalho: [0 para não tem ]'))
if dados["ctps"] != 0:
    dados["contratacao"] = int(input('Ano de contratação: '))
    dados["salario"] = float(input('Salário: R$'))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 50) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')
