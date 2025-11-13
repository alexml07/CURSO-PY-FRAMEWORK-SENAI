import streamlit as st
import math as mt

st.title("Classificação de níveis de glicose no sangue")
st.markdown(
    """
    | Nível de glicose |  Classificação  |
    |------------------|-----------------|
    |      0 -  70     |  Hipoglicêmica  |
    |     71 - 100     |     Normal      |
    |    101 - 140     |  Pré-diabetes   |
    |    141 ou mais   |   Diabetes      |
    """)
# Entrada de dados
glicose = st.number_input("Insira o nível de glicose no sangue (mg/dL):", min_value=0)
if st.button("Classificar"):
    if glicose <= 70:
        clas="Hipoglicemia"
    elif glicose <= 100:
        clas="Normal"
        st.balloons()
    elif glicose <=140:
        clas="Pré-diabetes"
    else:
        clas="Diabetes"
    st.write(f"Classificação: {clas}")
