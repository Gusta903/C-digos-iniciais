import os
print('Nome maior que 3 caracteres')
print('Idade maior que 0 e menor que 150')
print('Salário maior que 0')
print('Sexo F ou M')
print('Estado civil deve ser S, D, V ou C')
print(20*'--')


def obter_nome():
    while True:
        nome = str(input('Digite seu nome: '))
        if len(nome) > 3:
            return nome
        else:
            print('Nome invalido')

# Função para obter a idade


def obter_idade():
    try:
        while True:
            idade = int(input('Digite sua idade: '))
            if 0 <= idade <= 150:
                return idade
            else:
                print('Salário invalido')
    except ValueError:
        print('Deve ser um número inteiro')

# Função para obter o salário e ele tem q ser maior do que 0


def obter_salário():
    try:
        while True:
            salário = float(input('Digite o seu salário: '))
            if salário > 0:
                return salário
            else:
                print('Salário invalido')
    except ValueError:
        print('Deve ser um número inteiro')

# Função para obter o sexo da pessoa  e tem que ser F ou M caso não seja, o programa ira ler a té ser


def obter_sexo():
    while True:
        sexo = str(input('Digite seu sexo[F/M]: ')).upper().strip()[0]
        if sexo in ['F', 'M']:
            return sexo
        else:
            print('Sexo invalido ')

# Função para obter o estado civil da pessoa


def obter_estadocivil():
    while True:
        estadoc = str(input('Digite seu estado civil: ')).upper().strip()[0]
        if estadoc in ['S', 'C', 'D', 'V']:
            return estadoc
        else:
            print('Estado civil invalido')

# Pega os dados das pessoas e armazena aqui para aparecer no final


def cadastrar_pessoa():
    print("\nCadastrando uma nova pessoa...")

    nome = obter_nome()
    idade = obter_idade()
    salario = obter_salário()
    sexo = obter_sexo()
    estado_civil = obter_estadocivil()

    return {
        "nome": nome,
        "idade": idade,
        "salario": salario,
        "sexo": sexo,
        "estado_civil": estado_civil
    }


def main():
    # Inicializa com uma lista 'pessoas' para armazenar a quantidade de pessoas e os cadastros delas
    pessoas = []
    # Usa 'while True' para poder cadastrar varias pessoas
    while True:
        # usa-se .append para se você cadastrar 1 ira armazenar aqui com os cadastros 2 ira armazernar
        pessoas.append(cadastrar_pessoa())

        continuar = input("\nDeseja cadastrar outra pessoa? (s/n): ").lower()
        '''Após cadastrar uma pessoa  o programa ira perguntar se você quer continuar
        Caso responda 's' o terminal ira ser limpado e você ira cadastrar mais uma pessoa'''
        if continuar == 's':
            os.system('cls')
        else:
            break
    # Caso responda 'n' ira aparecer o cadastro de todas as pessoas
    print("\nCadastro finalizado. Informações cadastradas:")
    # O número de pessoas vai ser tederminado aqui
    for idx, pessoa in enumerate(pessoas, start=1):
        print(f"\nPessoa {idx}:")
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"Salário: {pessoa['salario']:.2f}")
        print(f"Sexo: {pessoa['sexo']}")
        print(f"Estado Civil: {pessoa['estado_civil']}")


if __name__ == "__main__":
    main()
