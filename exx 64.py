from random import randint
print('-' * 30)
print('Jogo do par ou impar')
print('-' * 30)
print('Digite qualquer outra coisa para parar')
n = 0
cont = 0
p = 0
v = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Você quer par ou impar [P/I]: ')).upper().strip()[0]
    computador = randint(0, 20)
    resultado = computador + n
    par = resultado % 2
    cont += 1
    if pi == 'P':
        if par == 0:
            print('Você ganhou!!')
            v += 1
        else:
            print('O computador ganhou!!')
            p += 1
    elif pi == 'I':
        if par == 1:
            print('Você ganhou!!')
            v += 1
        elif par == 0:
            print('O computador ganhou!!')
            p += 1
    else:
        print('Código deu errado tente novamente :(')
        break
    print('-'*20)
    print(f'O computador jogou {computador} e você jogou {n}')
    print(f'{computador} + {n} = {resultado}')
    print('-' * 20)
print(f'Você jogou {cont} vezes, ganhou {v}  e perdeu {p} vezes')
