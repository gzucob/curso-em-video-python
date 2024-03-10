from random import randint
pc = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram {pc}')
print(f'O maior valor foi {max(pc)}')
print(f'O menor valor foi {min(pc)}')
