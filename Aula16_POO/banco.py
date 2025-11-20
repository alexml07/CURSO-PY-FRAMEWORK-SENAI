class ContaPessoaFisica:#Super classe
    #1° Membro - Atributos privados
    __numeroDaConta:int
    __titular:str
    __saldo:float

    #2° Membro - Propriedades
    #Propriedade do numero da conta
    @property
    def _numeroDaConta(self) ->int :
        return self.__numeroDaConta
    @_numeroDaConta.setter
    def _numeroDaConta(self, numero:int) ->int :
        self.__numeroDaConta = numero
    #Propriedade titular
    @property
    def _titular(self) -> str:
        return self.__titular
    @_titular.setter
    def _titular(self, nome:str) ->str:
        self.__titular = nome
    #Propriedade saldo
    @property
    def _saldo(self) -> float:
        return self.__saldo
    @_saldo.setter
    def _saldo(self, saldo:float) ->float:
        self.__saldo = saldo
   
    #3° Membro - Construtor
    def __init__(self, numeroDaConta:int, titular:str, saldo:float):
        self._numeroDaConta = numeroDaConta
        self._titular = titular
        self._saldo = saldo
   
    #4° Membro - Métodos
    def depositar(self, deposito:float) -> float:
        self._saldo += deposito
    def saque(self, saque:float) -> float:
        self._saldo -= saque - 5.00

    #---Fim super classe---

class ContaPessoaJuridica(ContaPessoaFisica):#Sub classe da classe Conta Pessoa Fisica
    #1° Membro - Atributos
    __limite:float

    #2° Membro - Propriedades
    @property
    def _limite(self) -> float:
        return self.__limite
    @_limite.setter
    def _limite(self, limite) -> float:
        self.__limite = limite

    #3° Membro - Construtor
    def __init__(self, numeroDaConta, titular, saldo, limite):
        super().__init__(numeroDaConta, titular, saldo)
        self._limite = limite
   
    #4° Membro - Métodos
    def limiteDisponivel(self) -> float:
        return self._limite
    #----Fim sub classe----
class ContaPoupanca(ContaPessoaFisica):
    # 1º Membro - Atributos
    __taxaDeJuros=0.05

    # 2º Membro - Propriedades
    @property
    def __taxaDeJuros(self)->float:
        return self.__taxaDeJuros
    
    # 3º Membro - Construtor
    def __init__(self,numeroDaConta,titular,saldo):
        super().__init__(numeroDaConta,titular,saldo)
    
    # 4º Membro - Métodos
    def saque(self, saque:float) -> float:
        self._saldo-=saque
        return self._saldo
    def atualizarSaldo(self)->float:
        self.saldo+=self._saldo*self.__taxaDeJuros
        return self.saldo
#---------------Fim classes-------------

