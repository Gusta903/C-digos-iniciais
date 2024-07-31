n = float(input('Qual o sálario de um funcionario? R$'))
d = n + (n*15/100)
print('O salário que custava R${} passa a custar R${} com um aumento de 15%'
      .format(n, d))
