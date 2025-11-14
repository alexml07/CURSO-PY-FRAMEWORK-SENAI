import trianguloPOO as tl

# Instanciar a classe
tX=tl.triangulo()
tY=tl.triangulo()

# Entrada
print('Digite as medidas do triangulo X:')
tX.a=int(input('Digite a medida de a:'))
tX.b=int(input('Digite a medida de b:'))
tX.c=int(input('Digite a medida de c:'))
print('Digite as medidas do triangulo Y:')
tY.a=int(input('Digite a medida de a:'))
tY.b=int(input('Digite a medida de b:'))
tY.c=int(input('Digite a medida de c:'))

areax=tX.area()
areay=tY.area()

if areax>areay:
    saida='A área do triângulo X é maior que a área do Y.'
elif areay>areax:
    saida='A área do triângulo Y é maior que a área do X.'
else:
    saida='As áreas dos triângulos são iguais!'

# Saída

print(f"A área do triangulo X={areax:.1f}")
print(f"A área do triangulo Y={areay:.1f}")
print(saida)