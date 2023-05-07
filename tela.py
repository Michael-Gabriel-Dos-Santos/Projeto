import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome',size=(8,0)),sg.Input(size=(16,0),key='nome')],
            [sg.Text('Idade',size=(8,0)),sg.Input(size=(16,0),key='idade')],
            [sg.Text('Quais Provedores de E-mail são aceitos.')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('yahoo',key='yahoo')],
            [sg.Text('aceita cartão')],
            [sg.Radio('SIM','cartoes',key='aceitaCartao'),sg.Radio('NÃO','cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,180),default_value=0,orientation='h',size=(16,25),key='sliderVelocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(35,25))]


        ]
        self.janela = sg.Window("Dados do Usuário").layout(layout)

    def Iniciar(self):
         while True:
             self.button, self.values = self.janela.Read()
             nome = self.values['nome']
             idade = self.values['idade']
             aceita_gmail = self.values['gmail']
             aceita_outlook = self.values['outlook']
             aceita_yahoo = self.values['yahoo']
             aceita_Cartao = self.values['aceitaCartao']
             nao_aceita_Cartao = self.values['naoAceitaCartao']
             velocidade_script = self.values['sliderVelocidade']
             print(f'nome: {nome}')
             print(f'idade: {idade}')
             print(f'aceita gmail: {aceita_gmail}')
             print(f'aceita outlook: {aceita_outlook}')
             print(f'aceita yahoo: {aceita_yahoo}')
             print(f'aceita cartão: {aceita_Cartao}')
             print(f'não aceita cartão: {nao_aceita_Cartao}')
             print(f'Velocidade Scripts: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()
