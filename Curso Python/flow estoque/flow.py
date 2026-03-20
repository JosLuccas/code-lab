print ('-----Cadastro de Produto-----')

# nome_produto = str(input('\nDigite o nome do produto: '))
# quantidade_produto = int(input('Digite a quantidade deste produto: '))
# valor_produto = float(input('Digite o valor deste produto: '))
# descricao_produto = str(input('Digite a descrição do produto: '))
# nf_produto = int(input('Digite a Nota Fiscal do produto: '))

# print('\nProduto cadastrado com sucesso!')

# print(f'''
# Nome: {nome_produto}
# Quantidade: {quantidade_produto}
# Valor: R$ {valor_produto}
# Descrição: {descricao_produto}
# Nota Fiscal: {nf_produto}
# ''')

produtos = []

while True:
    nome = str(input("\nDigite o nome do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    valor = float(input("Digite o valor do produto: R$ "))

    produto = {
        "Nome" : nome,
        "Quantidade" : quantidade,
        "Valor": valor
    }

    produtos.append(produto)
    
    verificador = str(input("\nVocê deseja cadastra mais produtos? "))

    if verificador != "Sim":
        break

for produto in produtos:
    print(produto)
    