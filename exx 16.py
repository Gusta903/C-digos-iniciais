from random import choice
A = input('nome do aluno: ')
B = input('nome de outro aluno: ')
C = input('nome de outro aluno: ')
D = input('nome de outro: ')
lista = [A, B, C, D]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
