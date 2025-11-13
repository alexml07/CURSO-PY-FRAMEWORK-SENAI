import PySimpleGUI as sg
import numpy as np

# Lista para guardar o layout da janela
def main():
    layout= [
        [sg.Text(['Digite a quantidade de números que deseja inserir:'])],
        [sg.Input(key='n')],
        [sg.Button('ok'),sg.Button('Cancelar')]
    ]

    janela=sg.Window('Calculadora', layout)

    while True:
        evento, valores = janela.read()
        if evento==sg.WIN_CLOSED or evento=='Cancelar':
            janela.close()
            break
        elif evento=='ok':
            try:
                n=int(valores['n'])
                if n<=0:
                        sg.popup('Insira somente números positivos')
                        continue
                break
            except:
                sg.popup('Por favor, insira um valor válido')
    janela.close()
    numeros=[] # Outra lista

    for i in range(n):
        layout=[
            [sg.Text(f'Digite o {i+1}º número')],
            [sg.Input(key='Campeao')],
            [sg.Button('ok'), sg.Button("Cancelar")]
        ]
        janela=sg.Window('Entrada de número', layout)
        while True:
            eventos, valores=janela.read()
            if eventos==sg.WIN_CLOSED or eventos=='Cancelar':
                janela.close()
                break
            if eventos=='ok':
                try:
                    num=float(valores['Campeao'])
                    numeros.append(num)
                    break
                except:
                    sg.popup('Por favor, insira valores validos')
    janela.close()

    # Utilização dp numpy
    vetor=np.array(numeros)
    soma=np.sum(vetor) # Mesmo efeito de 'soma=np.sum(np.array(numeros))'
    media=np.mean(vetor) # Mesmo efeito de 'media=np.mean(np.array(numeros))'

    # Resultados
    resultado_layout = [
        [sg.Text('Elementos do vetor')],
        [sg.Text(','.join(map(str,vetor)))],
        [sg.Text(f'Soma dos elementos  = {soma}')],
        [sg.Text(f'Média dos elementos = {media}')],
        [sg.Button('Fechar')]
    ]
    resultado_janela=sg.Window('Resultado', resultado_layout)

    while True:
        eventoResultado=resultado_janela.read()
        if evento==sg.WIN_CLOSED or 'Fechar' in eventoResultado:
            resultado_janela.close()
            break
    resultado_janela.close()

if __name__=='__main__':
    main()