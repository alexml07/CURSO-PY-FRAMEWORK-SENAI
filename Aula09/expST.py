import streamlit as st

def porcentagem(cobaia):
    return (cobaia/total_cobaias)*100

def qtd(total):
    total+=quantidade
    return total

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
    total_cobaias=qtd(total_cobaias)
    if tipo=='C':
        total_coelhos=qtd(total_coelhos)
    elif tipo=='R':
        total_ratos=qtd(total_ratos)
    elif tipo=='S':
        total_sapos=qtd(total_sapos)

if total_cobaias>0:
    perc_coelhos = porcentagem(total_coelhos)
    perc_ratos = porcentagem(total_ratos)
    perc_sapos = porcentagem(total_sapos)
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