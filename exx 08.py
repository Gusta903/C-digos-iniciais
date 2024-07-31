P = float(input('Qual preço de um produto: R$'))
N = P - (P*5/100)
O = P - (P*15/100)
print('O produto que custava R${}, com uma Promoçao de 5% passa a custar R${}'
      .format(P, N))

print('O produto que custava R${}, com uma promoção de 15% passa a custa R${}'
      .format(P, O))
