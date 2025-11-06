from streamlit import header,write,text_input,button,warning,success,error,markdown
from math import sqrt,pow
def calculo(var_funcao):
    valor=(sqrt(var_funcao))/(2*a)
    return valor

header('Calculadora de Bhaskara')
markdown('Calculadora de raízes \n\nde uma equação de segundo grau')
write("ax² + bx + c = 0")

# Entrada de dados
a = text_input('Digite o valor de a:',icon="1️⃣")
b = text_input('Digite o valor de b:',icon="2️⃣")
c = text_input('Digite o valor de c:',icon="3️⃣")

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
            raiz=(-b+calculo(delta))
            success(f'A equação possui uma raiz real: {raiz}')
        else:
            raiz1=(-b+calculo(delta))
            raiz2=(-b-calculo(delta))
            write(f"A X': {raiz1:.4f}")
            write(f'A X": {raiz2:.4f}')
    except ValueError:
        error("Por favor, insira valores válidos para a, b e c.")
    except ZeroDivisionError:
        error("O valor de 'a' não pode ser zero em uma equação de segundo grau.")
    except:
        error("Aconteceu algum erro não previsto.")
