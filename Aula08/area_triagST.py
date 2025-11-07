import streamlit as st
import math as mt
import matplotlib.pyplot as plt
import numpy as np
# Calculando o perímetro e a área do triangulo

# def triangulo(A,B,C):
#     # --- Cálculo das Coordenadas (Usando trigonometria) ---
#     # V1 em (0, 0)
#     V1 = (0, 0)
#     # V2 no eixo X com comprimento C
#     V2 = (C, 0)
#     # Para V3 (x3, y3):
#     # 1. Calcular o ângulo beta (entre C e A) usando Lei dos Cossenos
#     cos_beta = (A**2 + C**2 - B**2) / (2 * A * C)
#     beta = np.arccos(cos_beta)

#     # 2. Calcular as coordenadas (x3, y3) usando V1, o lado A e o ângulo beta
#     x3 = A * np.cos(beta)
#     y3 = A * np.sin(beta)
#     V3 = (x3, y3)

#     # Criar a figura (V1, V2, V3, V1 para fechar o triângulo)
#     X = [V1[0], V2[0], V3[0], V1[0]]
#     Y = [V1[1], V2[1], V3[1], V1[1]]

#     fig, ax = plt.subplots()
#     ax.plot(X, Y, marker='o')
#     ax.set_aspect('equal', adjustable='box') # Garante proporção correta
#     st.pyplot(fig)

def triangulo(A: float, B: float, C: float, fator_reducao: float = 0.6):
    """
    Desenha um triângulo com lados A, B e C, ajustando o tamanho da figura.
    
    Args:
        A (float): Comprimento do lado A.
        B (float): Comprimento do lado B.
        C (float): Comprimento do lado C.
        fator_reducao (float): Fator pelo qual multiplicar o tamanho padrão da figura.
                               0.6 resulta em uma redução de 40%.
    """
    
    # --- ⚠️ Adicionando Verificação de Triângulo (Melhoria Essencial) ---
    if (A + B <= C) or (A + C <= B) or (B + C <= A):
        st.error(f"⚠️ Erro: Os lados ({A}, {B}, {C}) não formam um triângulo válido.")
        return

    # --- Cálculo das Coordenadas (Geometria) ---
    V1_x, V1_y = 0, 0
    V2_x, V2_y = C, 0

    try:
        # Lei dos Cossenos para achar o ângulo beta (entre C e A)
        cos_beta = (A**2 + C**2 - B**2) / (2 * A * C)
        # np.clip previne erros de ponto flutuante em arccos
        cos_beta = np.clip(cos_beta, -1.0, 1.0) 
        angulo_beta = np.arccos(cos_beta)

        # Coordenadas do Vértice 3 (V3)
        V3_x = A * np.cos(angulo_beta)
        V3_y = A * np.sin(angulo_beta)
        
    except Exception as e:
        st.error(f"Ocorreu um erro no cálculo trigonométrico: {e}")
        return

    # Criar a figura (V1, V2, V3, V1 para fechar o triângulo)
    X = [V1_x, V2_x, V3_x, V1_x]
    Y = [V1_y, V2_y, V3_y, V1_y]

    # --- 🖼️ Alteração Chave para Reduzir o Tamanho da Figura ---
    LARGURA_PADRAO = 6.4
    ALTURA_PADRAO = 4.8
    
    nova_largura = LARGURA_PADRAO * fator_reducao
    nova_altura = ALTURA_PADRAO * fator_reducao

    fig, ax = plt.subplots(figsize=(nova_largura, nova_altura))
    # -------------------------------------------------------------

    ax.plot(X, Y, marker='o')
    ax.set_aspect('equal', adjustable='box') # Garante proporção correta
    ax.set_title(f"Triângulo de Lados {A}-{B}-{C}")
    ax.set_xticks([]) # Remove marcações dos eixos para limpar
    ax.set_yticks([])
    
    st.pyplot(fig)

TITULO = "Cálculo de perímetro e área de um triângulo"
st.markdown(f"<h3 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)

# Entrada de dados
A = st.number_input("Medida de A (m):",min_value=0.0,format="%.2f",step=1.0,value=1.0)
B = st.number_input("Medida de B (m):",min_value=0.0,format="%.2f",step=1.0,value=1.0)
C = st.number_input("Medida de C (m) [em caso de trapézio informe a altura]:",min_value=0.0,format="%.2f",step=1.0,value=1.0)

eh_tri=(A+B)>C and (B+C)>A and (C+A>B)

if eh_tri:
    per_tri=A+B+C
    semiper=((A+B+C)/2)
    area=mt.sqrt(semiper*(semiper-A)*(semiper-B)*(semiper-C))
    st.success(f"A área do triangulo é: {area:.1f}")  
    st.success(f"O perímetro do triangulo é: {per_tri:.1f}")
    triangulo(A=A,B=B,C=C,fator_reducao=0.2)
else:
    per_tra=((A+B)*C)/2
    st.warning(f"As medidas {A} | {B} | {C} não podem formar um Triângulo!")
    st.success(f"Como um trapézio a área dele é igual a: {per_tra:.1f}")

