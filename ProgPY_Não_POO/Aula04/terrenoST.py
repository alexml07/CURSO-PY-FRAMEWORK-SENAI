# import streamlit as st

# st.title("Problema Terreno")
# # Entrada de dados
# st.write("Digite a largura do terreno (em metros):")
# largura = st.number_input("Largura (m):")
# st.write("Dig. o comprimento do terreno (m):")
# comprimento = st.number_input("Comprimento (m):")
# st.write("Digite o valor do metro quadrado em reais:")
# valor_m2 = st.number_input("Valor do m² (R$):")
# # Processamento de dados
# area = largura * comprimentopreco = area * valor_m2
# # Saída de dados
# st.write(f"A área do terreno é de {area} metros quadrados.")

import streamlit as st
import math as mt

TITULO = "Problema Retângulo"
st.title(TITULO)

# Entrada de dados
st.write("Digite o comprimento do retângulo")
comprimento = st.number_input("Comprimento (m):",min_value=0.0,format="%.2f",step=1.0,value=5.0)

st.write("Digite o comprimento do retângulo")
altura = st.number_input("Altura (m):",min_value=0.0,format="%.2f",step=1.0,value=2.5)

#Processamento de Dados
area = comprimento * altura
perimetro = 2*comprimento + 2*altura
# diagonal = (comprimento**2 + altura**2)**0.5
x = mt.pow(comprimento,2) + mt.pow(altura,2)
diagonal = mt.sqrt(x)

#Saída de dados
st.write(f"A área do terreno é de: {area}.")
st.write(f"O Perímetro é de: {perimetro}.")
st.write(f"O Perímetro é de: {diagonal:.2f}.")
