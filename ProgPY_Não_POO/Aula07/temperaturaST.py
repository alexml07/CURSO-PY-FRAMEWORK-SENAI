import streamlit as st
#from streamlit import bar_chart,columns,title,header,write,text_input,button,warning,success,error,markdown,number_input

def conv_c_f(t):
    return (t*1.8)+32

def conv_c_k(t):
    return t+273.15

def conv_f_c(t):
    return (t-32)*(5/9)

def conv_f_k(t):
    return conv_c_k(conv_f_c(t))

def conv_k_c(t):
    return t-273.15

def conv_k_f(t):
    return ((t-273.15)*9/5+32)

# Problema temperatura
st.sidebar.title("Conversos de temperatura")
st.title("Conversor de temperatura")
st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvin")
opcao=st.sidebar.radio(options=['Celsius', 'Kelvin', 'Fahrenheit'],key="opcao_radio",label="Selecionar")
# de_c=st.sidebar.checkbox("Celsius", key="temp_c")
# de_k=st.sidebar.checkbox("Kelvin", key="temp_k")
# de_f=st.sidebar.checkbox("Fahrenheit", key="temp_f")

# Entrada de dados
temp=st.number_input("Valor da temperatura:",format='%.2f',step=1.0)

# Processamento de dados
if st.button("Converter",icon='🌡️'):
    if opcao in "Celsius":
        st.write(f'{temp}ºC em Fahrenheit: {conv_c_f(temp):.2f}')
        st.write(f'{temp}ºC em Kelvin: {conv_c_k(temp):.2f}')
    elif opcao in "Fahrenheit":
        st.write(f'{temp}ºf em Celsius: {conv_f_c(temp):.2f}')
        st.write(f'{temp}ºf em Kelvin: {conv_f_k(temp):.2f}')
    elif opcao in "Kelvin":
        st.write(f'{temp}K em Celsius: {conv_k_c(temp):.2f}')
        st.write(f'{temp}K em Fahrenheit: {conv_k_f(temp):.2f}')
