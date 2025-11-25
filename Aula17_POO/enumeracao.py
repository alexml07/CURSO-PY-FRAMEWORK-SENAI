from enum import Enum

class Estados_Pedidos(Enum):
    PAGAMENTO_PENDENTE=0
    PROCESSAMENTO=1
    ENVIADO=2
    ENTREGUE=3
    CANCELADO=4
    SENAI="AULA DE SEGUNDA"

# Exemplo de uso
print(Estados_Pedidos(2))
print(Estados_Pedidos.CANCELADO)
print(Estados_Pedidos.ENVIADO.name) # Imprimir o nome do estado
print(Estados_Pedidos.ENTREGUE.value) # Imprimir o valor do estado
print(Estados_Pedidos(1).name) # Imprimir o nome do estado a partir do valor
print(Estados_Pedidos.SENAI.value) # Imprimir o valor do estado SENAI
