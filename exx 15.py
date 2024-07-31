import math
a = float(input('digite o angulo: '))
sen = math.sin(math.radians(a))
con = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print(' O angulo de {} tem o seno de {:.2f} \n O angulo de {} tem O cosseno de  {:.2f} \n O angulo de {} tem o tangente de {:.2f}'
      .format(a, sen, a, con, a, tan))
