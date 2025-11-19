## DOCUMENTAÇÃO GERAL
# Esta classe representa um Retângulo e calcula sua área, perímetro e diagonal,
# utilizando o conceito de Propriedades (Getters e Setters) para gerenciar a base e a altura.

class Retangulo:
    # 1º Membro - Atributos (Marcados como "privados" por convenção com __)
    __base: float
    __altura: float

    # 2º Membro - Propriedades (Mecanismos de acesso/modificação)
    @property
    def base(self): # Pegar valor do atributo base (Getter)
        return self.__base
    @base.setter
    def base(self, base: float): # Definir o valor do atributo base (Setter)
        self.__base = base
    @property
    def altura(self): # Pegar valor do atributo altura (Getter)
        return self.__altura
    @altura.setter
    def altura(self, altura: float): # Definir o valor do atributo altura (Setter)
        # Atenção: O comentário original dizia "Definir o valor do atributo base", mas foi ajustado para 'altura'
        self.__altura = altura
    
    # 3º Membro - Construtor (__init__)
    def __init__(self, base: float, altura: float):
        # Para chamar um Setter decorado com @property, não usamos parênteses como em um método comum.
        # Atribuímos o valor diretamente como se fosse um atributo.
        self.altura = altura # ## CORREÇÃO: Remove parênteses. Chama o setter 'altura'.
        self.base = base     # ## CORREÇÃO: Remove parênteses. Chama o setter 'base'.
    
    # 4º Membro - Métodos
    def area(self) -> float:
        # Para chamar o Getter (@property), não usamos parênteses.
        # Além disso, o método deve RETORNAR o valor calculado.
        return self.altura * self.base # ## CORREÇÃO: Adiciona 'return' e remove parênteses das propriedades.
    
    def perimetro(self) -> float:
        # A fórmula do perímetro é (base*2) + (altura*2) ou 2*(base + altura).
        # A fórmula original tinha um erro de lógica (usava altura duas vezes)
        # Além disso, o método deve RETORNAR o valor calculado.
        return (self.base * 2) + (self.altura * 2) # ## CORREÇÃO: Adiciona 'return' e corrige a fórmula para usar 'base' e 'altura'.
    
    def diagonal(self) -> float:
        # A importação deve ser feita no início do arquivo ou método, mas vamos manter aqui.
        from math import sqrt, pow
        # Para chamar os Getters (@property), não usamos parênteses.
        # Além disso, o método deve RETORNAR o valor calculado.
        return sqrt(pow(self.base, 2) + pow(self.altura, 2)) # ## CORREÇÃO: Adiciona 'return' e remove parênteses das propriedades.
    
    def dadosRetangulo(self) -> str: # ## CORREÇÃO: Adiciona 'self' como primeiro parâmetro.
        # Este método precisa receber 'self' para acessar os outros métodos e propriedades da instância.
        saida = f'''Area = {self.area():.2f}\n
        Perimetro = {self.perimetro():.2f}\n
        Diagonal = {self.diagonal():.2f}\n'''
        # Usei {:.2f} para formatar as saídas com duas casas decimais.
        return saida
# Fim classe

# --- PROGRAMA PRINCIPAL ---

# Entrada de dados
# Note que os prompts de input foram ajustados para maior clareza.
try:
    base = float(input('Digite a base do retângulo: ')) # ## CORREÇÃO: Altera o prompt para 'base'.
    altura = float(input('Digite a altura do retângulo: '))
    
    # Instanciar o objeto do tipo retângulo
    retangulo = Retangulo(base, altura)
    
    # Saída de dados
    print('\n--- Dados do Retângulo ---')
    print(retangulo.dadosRetangulo())

except ValueError:
    print("\n⚠️ Erro: Certifique-se de digitar números válidos para a base e altura.")