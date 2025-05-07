def cadastro_pessoa(num):
    for i in range(num):

        nome = input('Informe o nome: ')
        valor = input('Informe o valor da venda: ')

        pessoa = {
            'Nome': nome,
            'Valor': valor,
        }

        list_cadastro.append(pessoa)

list_cadastro = []

qtd = int(input('Quantas pessoas?: '))
cadastro_pessoa(qtd)
print(list_cadastro)
