P = float(input('Qual o preço de um produto? R$'))
p = P + (P*9/100)
V = P - (P*13/100)
print('O valor de um produto custa R${} à vista recebe desconto de 9% e custa R${}'
      .format(P, V))

print('O valor de um produto custa R${} parcelado ele custa R${}'
      .format(P, p))
