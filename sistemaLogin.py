import PySimpleGUI as sg

class TelaPython:
    sg.change_look_and_feel('black')

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Button('criar login')],
    [sg.CloseButton('voltar')],
    [sg.Text('',key='mensagem')],
]

window = sg.Window('Login',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        ## teste por nao ter banco de dados ##
        senha_correta = 'vasco'
        usuario_correto = 'michael'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso!')
        else:
            window['mensagem'].update('senha ou usuário íncorreto')

