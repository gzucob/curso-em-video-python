frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print(f'Temos um palímdromo!')
else:
    print(f'A frase não é um palíndromo.')