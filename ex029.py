import random
vel = random.randint(0, 200)
multa = (vel - 80) * 7
if vel <= 80:
    print(f'Velocidade Atual: {vel}\nVocê está dentro do limite de 80km/h. Boa viagem!')
else:
    print(f'Velocidade Atual: {vel}\nVocê está acima do limite de 80km/h!\nO valor da sua multa é R${multa:.2f}.')
