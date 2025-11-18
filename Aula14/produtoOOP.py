import produtoC as p # Importar o modulo

# Entrada de dados
print('Entre com os dados do produto: ')
nome=input('Nome: ')
preco=int(input('Preço: R$ '))
saldo=int(input('Quantidade: '))

# Instanciar o objeto
ps=p.Produto(nome, preco, saldo)

# Saída de dados
print(ps.dadosDoProduto())