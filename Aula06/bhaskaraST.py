from streamlit import header,write,text_input,button,warning,success,error,markdown
from math import sqrt,pow
def calculo(delta):
    (sqrt(delta))/(2*a)
    

header('Calculadora de Bhaskara')
markdown('Calculadora de raízes \n\nde uma equação de segundo grau')
write("ax² + bx + c = 0")

# Entrada de dados
a = text_input('Digite o valor de a:')
b = text_input('Digite o valor de b:')
c = text_input('Digite o valor de c:')

# Processamento de dados
if button('Calcular raízes'):
    try:
        a=float(a)
        b=float(b)
        c=float(c)
        delta=pow(b,2)-4*a*c
        if delta < 0:
            warning('A equação não possui raízes reais.')
        elif delta==0:
            raiz=(-b+sqrt(delta))/(2*a)
            success(f'A equação possui uma raiz real: {raiz}')
        else:
            raiz1=((-b+sqrt(delta))/(2*a))
            raiz2=((-b-sqrt(delta))/(2*a))
            write(f"A X': {raiz1:.4f}")
            write(f'A X": {raiz2:.4f}')
    except:
        error("Por favor, insira valores válidos para as 3 variáveis.")