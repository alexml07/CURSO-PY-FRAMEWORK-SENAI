''' teste de comentário
multi-linhas
'''
# Para comentar uma única linha, use o símbolo cerquilha (#) no início da linha.

# Problema medidas terreno

largura: float
comprimento: float
# Entrada de dados
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
valor_metro_quadrado = float(input("Digite o valor do metro quadrado (em reais): "))
# Processamento de dados
area = largura * comprimento
custo_total = area * valor_metro_quadrado
# Saída de dados
print(f"A área do terreno é: {area:.2f} metros quadrados")
print(f"O custo total do terreno é: R$ {custo_total:.2f}")
