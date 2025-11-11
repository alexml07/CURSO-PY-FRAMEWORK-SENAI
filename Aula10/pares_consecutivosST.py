import streamlit as st

# Problema de soma de 5 pares consecutivos

st.title('Calculadora pares consecutivos')
# Entrada de dados
numero=st.number_input('Digite um numero inteiro', step=1)
botao=st.button('Calcular')
if botao:
    if (numero%2) != 0:
        st.write('Impar')
    else