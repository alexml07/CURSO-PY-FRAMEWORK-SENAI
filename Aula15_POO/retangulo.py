class Retangulo:
    # Membros da clsse
    # 1º Membro - Atributos
    __base:float
    __altura:float

    # 2º Membro - Propriedades
    @property
    def base(self): # Pegar valor do atributo base
        return self.__base
    @base.setter
    def base(self, base:float): # Definir o valor do atributo base
        self.__base=base
    @property
    def altura(self): # Pegar valor do atributo altura
        if altura<0:
            altura=0
        return self.__altura
    @altura.setter
    def altura(self, altura:float): # Definir o valor do atributo base
        self.__altura=altura
    
    # 3º Membro - Construtor
    def __init__(self,base:float,altura:float):
        self.altura=altura
        self.base=base
    
    # 4º Membro - Métodos
    def area(self) -> float:
        return self.altura*self.base
    
    def perimetro(self) -> float:
        return (self.base*2)+(self.altura*2)
    
    def diagonal(self) -> float:
        from math import sqrt, pow
        return sqrt(pow(self.base,2)+pow(self.altura,2))
    
    def dadosRetangulo(self) -> str:
        saida=f'''Area = {self.area()}\n
Perimetro={self.perimetro()}\n
Diagonal={self.diagonal()}\n'''
        return saida
# Fim classe

# Inicio programa principal
# Entrada de dados
base=float(input('Digite a altura do retângulo: '))
altura=float(input('Digite a altura do retângulo: '))
# Instanciar o objeto do tipo retângulo
retangulo=Retangulo(base,altura)
#Saída de dados
print(retangulo.dadosRetangulo())