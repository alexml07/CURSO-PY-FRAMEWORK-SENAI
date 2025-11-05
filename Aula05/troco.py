# Calcula o troco

import streamlit as st
import math as mt

TITULO = "Troco Caixa"
st.title(TITULO)

# Entrada de dados
vr_unit = st.number_input("Preço unitário do Produto:",min_value=0.00,format="%.2f",step=1.00,value=0.00)
qt_comprada = st.number_input("Quantidade comprada:",min_value=0,step=1,value=1)
vr_recebido = st.number_input("Dinheiro recebido:",min_value=vr_unit*qt_comprada,format="%.2f",step=1.00,value=vr_unit*qt_comprada)

#Processamento de Dados
troco = vr_recebido-(vr_unit*qt_comprada)

#Saída de dados
st.write(f"TROCO: {troco:.2f}.")
