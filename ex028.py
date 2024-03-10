import random
import time
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
user = int(input('Em que número eu pensei? '))
time.sleep(2)
pc = random.randint(0, 5)
if user == pc:
    print('PARABÉNS! Você acertou!')
else:
    print(f'ERRADO! O número correto é {pc}.')
