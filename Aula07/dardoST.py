from streamlit import bar_chart,columns,title,header,write,text_input,button,warning,success,error,markdown,number_input

def grafico(datsu1,datsu2,datsu3):
    # Apresentação de grafico
    bar_chart([datsu1 ,datsu2,datsu3],
                use_container_width=True, height=200, color="#eaff00")

title('🎯Simulação de lançamento de Dardos🎯')
# Simulação de lançamento de 3 dardos. O objetivo do aplicativo é mostrar o dardo com a maior distancia
# Entrada de dados
header("Inserir as tres distancias dos dardos lançados pelo jogador.")
col1, col2, col3 = columns(3)
with col1:
    dardo1=number_input("Dig. 1ª dardo:",min_value=0)
with col2:
    dardo2=number_input("Dig. 2ª dardo:",min_value=0)
with col3:
    dardo3=number_input("Dig. 3ª dardo:",min_value=0)
maior_dist=max(dardo1,dardo2,dardo3)

# Estrutura de controle de decisão
if (dardo1>dardo2) and (dardo1>dardo3):
    dardo_venc='Dardo 1'
elif (dardo2>dardo1) and (dardo2>dardo3):
    dardo_venc='Dardo 2'
elif (dardo3>dardo1) and (dardo3>dardo2):
    dardo_venc='Dardo 2'
elif (dardo1==dardo2) or (dardo2==dardo3) or (dardo1==dardo3):
    dardo_venc='Empate'

# Saída de dados
if button('Apresentar resultados de lançamento'):
    if dardo_venc=="Empate":
        write('Houve empate sem vencedores')
    else:
        write(f"O dardo com a maior distância e {dardo_venc} com {maior_dist}")
        grafico(dardo1,dardo2,dardo3)