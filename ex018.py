import math
a = float(input('Diga um angulo qualquer: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'O angulo é {a}\nO seno é {s:.2f}\nO cosseno é {c:.2f}\nE a tangente é {t:.2f}')