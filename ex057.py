sexo = str(input('Informe o seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Opção inválida. Por favor, informe seu sexo [F/M]: ')).strip().upper()[0]
print(f'Sexo registrado com sucesso.')
