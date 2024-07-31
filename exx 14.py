import math
co = float(input('digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('A medida da hipotenusa é {:.2f}'.format(h))
