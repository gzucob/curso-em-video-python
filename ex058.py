from random import randint
tentativas = 0
pc = randint(0, 10)
print('Sou seu computador...\nAcabei de pensei em um número de 0 a 10.')
var = int(input('Você consegue adivinhar qual é? '))
while pc != var:
    if var < pc:
        print('Mais... Tente novamente.')
    else:
        print('Menos... Tente novamente.')
    tentativas += 1
    var = int(input(f'Tente outra vez: '))
print(f'Parabéns! Você acertou com {tentativas} tentativas.')
