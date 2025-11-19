import streamlit as st

# Problema senha fixa
st.title('Idades e Alturas')

# Entrada de dados
MAXIMO=10
nomes = []
idades =[]
alturas=[]
nomes_menor16 = []
soma_alt=0
qtde_menor16=0
while True:
    n=int(st.number_input('Digite o nr. de pessoas (máximo de 10 pessoas): '))
    if n>MAXIMO:
        st.error('Excedeu o nr. máximo de 10 pessoas.')
        continue
    else:
        break
qtde=int(n+1)
for i in range(1,qtde):
    nomes.append=st.text_input(f'Digite o nome da {i}ª pessoa: ')
    idades.append=st.number_input(f'Idade (anos inteiro) de {nomes[i-1]}: ')
    alturas.append=st.number_input(f'Altura (metros) {nomes[i-1]}: ')
    soma_alt+=alturas[i-1]
    if idades[i-1]<16:
        nomes_menor16.append=nomes[i-1]
        qtde_menor16+=1

# Processamento
media_altura=float(soma_alt/n)
perc_menor16=float((qtde_menor16/n)*100)

# Saída de dados
st.success(f'A média da altura de todas as {n} pessoas é: {media_altura:.2f}')
if qtde_menor16==0:
    st.warning(f'Não tem nenhuma pessoa com menos de 16 anos.')
else:
    st.success(f'A quantidade de pessoas com menos de 16 anos é: {qtde_menor16:}')
    st.success(f'O nome da 1ª pessoa: {nomes_menor16[0]}')
    for i in range(1,qtde_menor16+1):
        st.success(f'O nome da {i}ª pessoa: {nomes_menor16[i]}')

# ==========

# # Entrada de dados
# usuario_entrada=st.text_input('Nome do usuário')
# senha_entrada=st.text_input('Senha',type='password')
# botao=st.button('Logar')

# # Tentativas de acesso
# MAXIMO_TENTATIVAS=3

# if 'tentativas' not in st.session_state:
#     st.session_state.tentativas=0

# # Estrutura de controle em loop
# if botao is True:
#     if st.session_state.tentativas>=MAXIMO_TENTATIVAS:
#         st.error('Máximo de tentativas atingido. Acesso bloqueado')
#     else:
#         while st.session_state.tentativas < MAXIMO_TENTATIVAS:
#             if usuario_entrada==USUARIO and senha_entrada==SENHA:
#                 st.success('Login bem sucedido!')
#                 st.session_state.tentativas=0
#                 break
#             else:
#                 st.session_state.tentativas += 1
#                 st.warning(f'Credenciais invalidas. Tentativa {st.session_state.tentativas} de {MAXIMO_TENTATIVAS}')
#                 break
