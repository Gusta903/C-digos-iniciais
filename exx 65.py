contH = 0
contM = 0
tot18 = 0
while True:
    print(20 * '-')
    I = int(input('Idade: '))
    G = ' '
    while G not in 'FM':
        G = str(input('Gênero [F/M]: ')).upper().strip()[0]
    if I >= 18:
        tot18 += 1
    if G == 'M':
        contH += 1
    if G == 'F':
        if I < 20:
            contM += 1
    print(20 * '-')
    C = ' '
    while C not in 'SN':
        C = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if C == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é de {tot18}')
print(f'O total de homens é de {contH}')
print(f'O total de mulheres com menos de 18 anos é de {contM}')
print('Acabou')
