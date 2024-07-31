
while True:
    n = float(input('Digite o número da sua tabuada: '))
    if n < 1:
        print('Programa de tabuada errado ')
        break
    else:
        for x in range(1, 11):
            print(f'{n} x {x} x {n*x}')
