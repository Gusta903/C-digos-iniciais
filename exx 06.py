n = float(input('quanto dinheiro você tem? R$'))
Dolar = n / 5.20
Euro = n / 5.55
Yene = n / 0.033
print('Com R${:.2f} você pode comprar US${:.2f}'.format(n, Dolar))
print('Com R${:.2f} você pode comprar Eur{:.2f}'.format(n, Euro))
print('Com R${:.2f} você pode comprar Yene{:.2f}'.format(n, Yene))
