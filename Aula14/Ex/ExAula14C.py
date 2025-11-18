class Pessoa:
    # Atributos
    nome:str
    idade:int

    # Construtor
    def __init__(self, nome:str='', idade:int=0):
        self.nome=nome
        self.idade=idade

    # Metodos
    def eh_mais_velha(self, outra_idade) -> bool:
        return self.idade>outra_idade
    
class Funcionario:
    # Atributos
    nome:str
    salario:float

    # Construtor
    def __init__(self, nome:str='', salario:float=0):
        self.nome=nome
        self.salario=salario

    # Metodos
    def salario_medio(self, outro) -> float:
        return (self.salario+outro)/2
    

#===
#     def adicionarProdutos(self, quantidade) -> int:
#         self.saldo=self.saldo+quantidade
#         return self.saldo
#     def removerProdutos(self, quantidade) -> int:
#         self.saldo=self.saldo-quantidade
#         return self.saldo
#     def dadosDoProduto(self) -> str:
#         saida=f'''
# Dados do poduto
# \tNome do produto: {self.nome}
# \tValor de compra do produto: R$ {self.preco:.2f}
# \tQuantidade em estoque: {self.saldo}
# \tValor total em estoque: R$ {self.valorTotalEmEstoque():.2f}
#             '''
#         return saida