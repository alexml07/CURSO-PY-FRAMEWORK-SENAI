import streamlit as st

# Problema experiencias com cobaias
st.title("Laboratorio de cobaias")
# Declaração de variáveis de controletotal_cobaias = 0total ratos = 0total_sapos = 0total_coelhos = 0
# Entrada de dados
n=st.number_input("Digite o numero de experimentos:", min_value=1, step=1)
total_cobaias=total_coelhos=total_ratos=total_sapos=0
#Estrutura de controle - PARA - Loop determinado em python
for i in range(n):
    quantidade=st.number_input(f"Experimento {i+1} - Quantidade de cobaias utilizadas:", min_value=1,step=1)
    tipo=st.selectbox(f"Experimento {i+1} - Tipo de cobaia: (C:Coelho, R:Rato, S:Sapo):", options=['C','R','S'])

    # Processamento de dados
    total_cobaias+=quantidade
    if tipo=='C':
        total_coelhos+=quantidade
    elif tipo=='R':
        total_ratos+=quantidade
    elif tipo=='S':
        total_sapos+=quantidade

if total_cobaias>0:
    perc_coelhos = (total_coelhos/total_cobaias)*100
    perc_ratos = (total_ratos/total_cobaias)*100
    perc_sapos = (total_sapos/total_cobaias)*100
else:
    perc_coelhos=perc_ratos=perc_sapos=0

# Saída de dados
st.subheader("Resultados:")
st.write("Total de cobaias utilizados:", total_cobaias)
st.write("Total de coelhos utilizados:", total_coelhos)
st.write("Total de ratos utilizados:", total_ratos)
st.write("Total de sapos utilizados:", total_sapos)

# Percentual
st.write(f"Percentual de coelhos: {perc_coelhos:.2f}")
st.write(f"Percentual de ratos: {perc_ratos:.2f}")
st.write(f"Percentual de sapos: {perc_sapos:.2f}")