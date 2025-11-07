import streamlit as st
import math as mt
import matplotlib.pyplot as plt
import numpy as np
# Calculando o perímetro e a área do triangulo

TITULO = "Cálculo de perímetro e área de um triângulo"
st.markdown(f"<h3 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)

# Entrada de dados
A = st.number_input("Medida de A (m):",min_value=0.0,format="%.2f",step=1.0,value=1.0)
B = st.number_input("Medida de B (m):",min_value=0.0,format="%.2f",step=1.0,value=1.0)
C = st.number_input("Medida de C (m) [em caso de trapézio informe a altura]:",min_value=0.0,format="%.2f",step=1.0,value=1.0)

if (A+B)>C and (B+C)>A and (C+A>B):
    per_tri=A+B+C
    semiper=((A+B+C)/2)
    area=mt.sqrt(semiper*(semiper-A)*(semiper-B)*(semiper-C))
    st.success(f"A área do triangulo é: {area:.1f}")  
    st.success(f"O perímetro do triangulo é: {per_tri:.1f}")
else:
    per_tra=((A+B)*C)/2
    st.warning(f"As medidas {A} | {B} | {C} não podem formar um Triângulo!")
    st.success(f"Como um trapézio a área dele é igual a: {per_tra:.1f}")

# A, B e C são os comprimentos dos lados
lado_a = A
lado_b = B
lado_c = C # Exemplo de triângulo retângulo (3, 4, 5)

# --- Cálculo das Coordenadas (Usando trigonometria) ---
# V1 em (0, 0)
V1 = (0, 0)
# V2 no eixo X com comprimento C
V2 = (lado_c, 0)

# Para V3 (x3, y3): 
# 1. Calcular o ângulo beta (entre C e A) usando Lei dos Cossenos
cos_beta = (lado_a**2 + lado_c**2 - lado_b**2) / (2 * lado_a * lado_c)
beta = np.arccos(cos_beta)

# 2. Calcular as coordenadas (x3, y3) usando V1, o lado A e o ângulo beta
x3 = lado_a * np.cos(beta)
y3 = lado_a * np.sin(beta)
V3 = (x3, y3)

# ----------------------------------------------------

# Criar a figura (V1, V2, V3, V1 para fechar o triângulo)
X = [V1[0], V2[0], V3[0], V1[0]]
Y = [V1[1], V2[1], V3[1], V1[1]]

fig, ax = plt.subplots()
ax.plot(X, Y, marker='o')
ax.set_aspect('equal', adjustable='box') # Garante proporção correta

st.pyplot(fig)
