L = float(input('Uma distançia em metros: '))
K = L/1000
H = L/100
Dc = L/10
Dm = int(L*10)
Cm = int(L*100)
Mm = int(L*1000)
print('A medida de {}m corresponde a; '.format(L))
print('{}Km \n {}Hm \n {}Dc \n {}Dm \n {}Cm \n {}MM'
      .format(K, H, Dc, Dm, Cm, Mm))
