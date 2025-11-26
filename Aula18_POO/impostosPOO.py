from abc import ABC, abstractmethod

class Contribuintes(ABC):
    __nome:str
    __rendaAnual:float
    __imposto:float
    @property
    def _nome(self)->str:
        return self.__nome
    @_nome.setter
    def _nome(self,nome:str)->str:
        self.__nome=nome
    @property 
    def _rendaAnual(self)->float:
        return self.__rendaAnual
    @_rendaAnual.setter
    def _rendaAnual(self,rendaAnual:float)->float:
        self.__rendaAnual = rendaAnual
        
    @property 
    def _imposto(self)->float:
        return self.__imposto
    @_imposto.setter
    def _imposto(self,imposto:float)->float:
        self.__imposto=imposto

    def __init__(self,nome:str,rendaAnual:float,imposto:float=0):
        self._nome=nome
        self._rendaAnual=rendaAnual
        self._imposto=imposto

    def impostoSave(self,vrImp:float)->None:
        self._imposto=vrImp

    @abstractmethod
    def calcImposto(self)->float:
        pass
# ---Fim super classe ---
class PesFis(Contribuintes):
    __gastosSaude:float
    @property
    def _gastosSaude(self)->float:
        return self.__gastosSaude
    @_gastosSaude.setter
    def _gastosSaude(self,valorGasto:float)->float:
        self.__gastosSaude=valorGasto
    def __init__(self,nome:str,rendaAnual:float,valorGasto:float):
        super().__init__(nome,rendaAnual,valorGasto)
        self._gastosSaude=valorGasto

    def calcImposto(self)->None:
        if super()._rendaAnual<20000:
            imposto=super()._rendaAnual*0.15
        else:
            imposto=super()._rendaAnual*0.25
        imposto=imposto-(self._gastosSaude*0.5)
        self.impostoSave(imposto)

class PesJur(Contribuintes):
    __nrFunc:int
    @property
    def _nrFunc(self)->int:
        return self.__nrFunc
    @_nrFunc.setter
    def _nrFunc(self,nrFunc:float)->float:
        self.__nrFunc=nrFunc
    def __init__(self,nome:str,rendaAnual:float,nrFunc:float):
        super().__init__(nome,rendaAnual,nrFunc)
        self._nrFunc=nrFunc

    def calcImposto(self)->None:
        if self._nrFunc>10:
            imposto=super()._rendaAnual*0.14
        else:
            imposto=super()._rendaAnual*0.16
        self.impostoSave(imposto)

n=0
lista=[]
PF:PesFis
PJ:PesJur

n=int(input('\nDigite quantos contribuintes a calcular: '))
for i in range(n):
    nome=input(f'\nNome do {i+1}º contribuinte: ')
    vrRenda=float(input('Valor da Renda: '))
    gastoSaude=float(input('Despesas com Saúde (se pessoa Jurídica digite 0 [zero]): '))
    nrFunc=float(input('Qtde. de funcionários (se pessoa Física digite 0 [zero]): '))
    if gastoSaude>0:
        PF=PesFis(nome,vrRenda,gastoSaude)
        PF.calcImposto     
        lista.append(f'A Pessoa Física {PF._nome} com renda {PF._rendaAnual:.2f} pagou {PF._imposto} e ficou o líquido de {PF._rendaAnual-PF._imposto:.2f}')
    elif nrFunc>0:
        PJ=PesJur(nome,vrRenda,nrFunc)
        PJ.calcImposto
        lista.append(f'A Pessoa Jurídica {PJ._nome} com renda {PJ._rendaAnual:.2f} pagou {PJ._imposto} e ficou o líquido de {PJ._rendaAnual-PJ._imposto:.2f}')
    else:
        raise ValueError("\nNão foram digitados valores válidos para qualificar como Pessoa Jurídica nem Física.")

print('\n\nImpostos Calculados:\n')
for P in lista:
    print(P)
