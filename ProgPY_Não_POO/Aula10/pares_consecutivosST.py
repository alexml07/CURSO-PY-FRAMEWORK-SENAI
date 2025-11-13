import streamlit as st

# Problema de soma de 5 pares consecutivos

st.title('Calculadora pares consecutivos')
# Entrada de dados
numero=st.number_input('Digite um numero inteiro', step=1)
botao=st.button('Calcular')
contagem=0
soma=0
if botao:
    if (numero%2)!=0:
        numero+=1
    while contagem<5:
        soma+=numero
        numero+=2
        contagem+=1
    st.write(soma)