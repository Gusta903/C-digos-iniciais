nome = str(input('digite seu nome completo: ')).strip()
print('Seu nome em letras maiusculas: {}'.format(nome.upper()))
print('Seu nome em letras minusculas: {}'.format(nome.lower()))
print('Quantidade de letras que seu nome tem: {}'.format(
    len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} ele tem {} letras'.format(
    separa[0], len(separa[0])))
