class Terreno:
    #Membros da classe

    #1° Membro - Atributos
    __largura:float
    __comprimento:float

    #2° Membros - Propriedades

    #Propriedades largura
    @property
    def largura(self):
        return self.__largura
    @largura.setter
    def largura(self, largura: float):
        self.__largura = largura
    #Propriedade do comprimento
    @property
    def comprimento(self):
        return self.__comprimento
    @comprimento.setter
    def comprimento(self, comprimento:float):
        self.__comprimento = comprimento
   
    #3° Membro - Construtor
    def __init__(self, largura:float, comprimento: float):
        self.comprimento = comprimento
        self.largura = largura

    #4° Membro - Metodos
    def __area(self) -> float:
        return self.comprimento * self.largura
   
    def __preco(self, preco: float) -> float:
        return self.__area() * preco
   
    def dadosTerreno(self, preco: float) -> str:
        saida = f'''\tLargura: {self.largura}
        Comprimento: {self.comprimento}
        Area: {self.__area():.2f}
        Preco: {self.__preco(preco):.2f}'''
        return saida
#-----Fim classe-------

#Inicio programa principal
#Entrada de dados
try:
    largura = float(input("Digite a largura do terreno: "))
    comprimento = float(input("Digite o comprimento do terreno: "))
    preco = float(input("Digite o preco do metro quadrado: "))
    #Instanciar o objeto do tipo terreno
    terreno = Terreno(largura, comprimento)
    #Saida de dados
    print(terreno.dadosTerreno(preco))
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número válido.")