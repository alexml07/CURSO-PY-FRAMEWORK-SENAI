import calculadora as c
# Instanciação do objeto
circulo=c.calculadora()
# Entrada
raio=float(input('Digite o valor do raio: '))
# Processamento
circunferencia=circulo.circunferencia(raio)
area=circulo.area(raio)
# Saida
print(f''' Circunferência: {circunferencia:.2f}
        Area: {area:.2f}
        PI: {circulo.PI}
''')