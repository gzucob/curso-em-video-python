n = float(input('Qual o preço do produto? R$'))
d = n - (n * 5 / 100)
print(f'O valor com 5% de deconto é R${d:.2f}, o desconto foi de R${n * 5 / 100:.2f}')
