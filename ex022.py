nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiusculas {}'.format(nome.upper()))
print('Seu nome em letras minusculas {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))



