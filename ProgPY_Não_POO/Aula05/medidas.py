# Problemas medidas

import streamlit as st
import math as mt

TITULO = "Cálculo de área de um quadrado, triângulo e um trapézio"
# st.markdown(f"<h1 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)
# st.markdown(f"<h2 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)
# st.markdown(f"<h4 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)
# st.markdown(f"<h5 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)
# st.markdown(f"<h6 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)



# Entrada de dados
A = st.number_input("Medida de A (m):",min_value=0.0,format="%.2f",step=1.0,value=1.0)
B = st.number_input("Medida de B (m):",min_value=0.0,format="%.2f",step=1.0,value=1.0)
C = st.number_input("Medida de C (m):",min_value=0.0,format="%.2f",step=1.0,value=1.0)

# Processamento de dados
areaQuadrado = mt.pow(A,2)
areaTriangulo = (A*B)/2
areaTrapézio = ((A+B)*C)/2

# Saída de Dados
st.markdown("<h3 style='text-align: left;'>Resultados:</h2>", unsafe_allow_html=True)
st.write(f"A área do Quadrado é: {areaQuadrado}.")
st.write(f"A área do Retangulo é: {areaTriangulo}.")
st.write(f"A área do Trapézio é: {areaTrapézio}.")
