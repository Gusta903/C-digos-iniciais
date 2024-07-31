n = 0
soma = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A quantidade de números foi {cont}')
print(f'A soma entre eles foi  {soma} ')
