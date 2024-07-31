D = int(input('Quantos dias alugados: '))
Km = float(input('Quantos km rodados: '))
P = (D*60) + (Km * 0.15)
print('O valor à pagar é  de R${:.2f}'.format(P))
