from calc import calculadora

# Instanciação do objeto

# Entrada
raio=float(input('Digite o valor do raio: '))
# Processamento
circunferencia=calculadora.circunferencia(raio)
area=calculadora.area(raio)
# Saida
print(f''' Circunferência: {circunferencia:.2f}
        Area: {area:.2f}
        PI: {calculadora.PI}
''')