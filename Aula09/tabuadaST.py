import streamlit as st

TITULO="Tabuada"

# Tabuada
st.title(TITULO)
st.set_page_config(TITULO)
# Entrada de dados
n=None
try:
    n=int(st.text_input("Deseja a tabuada de qual número:"))
    for i in range(1,11):
        saida = f" {n:2} x {i:2} = {n*i:2}"
        st.markdown(f"""{saida}""")
except ValueError:
    if n is None:
        st.warning('Digite algum valor')
    else:
        st.error("Digite somente números inteiros")
except Exception as e:
    st.warning(f'O erro foi: {e}')

