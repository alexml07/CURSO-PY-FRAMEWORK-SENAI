import produtoPOO as p # Importar o modulo

p1=p.Produto() # Instanciar o objeto

# Entrada de dados
print('Digite os dados do produto')
p1.nome=input('\tNome: ')
p1.preco=float(input('\tPreco: R$ '))
p1.saldo=int(input('\tQuantidade: '))

# Saída de dados 1
# print('Dados do produto')
# print(f'\tNome do produto: {p1.nome}')
# print(f'\tValor de compra: {p1.preco:.2f}')
# print(f'\tQuantidade em estoque: {p1.saldo}')
# print(f'Valor total em estoque: R$ {p1.valorTotalEmEstoque():.2f}')

# Adicionar produto
print(p1.dadosDoProduto())
q=int(input('Digite o número de produtos a ser adicionado ao estoque: '))
p1.adicionarProdutos(q)
# Saída de dados 2
print('-- Dados atualizados --')
print(p1.dadosDoProduto())

# Remover produto
q=int(input('Digite o número de produtos a ser adicionado ao estoque: '))
p1.removerProdutos(q)
# Saída de dados 3
print('-- Dados atualizados --')
print(p1.dadosDoProduto())

