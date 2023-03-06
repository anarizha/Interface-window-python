from PySimpleGUI import PySimpleGUI as sg

#Layout da interface
sg.theme('Reddit')
layout = [
    [sg.Text('usuário'), sg.Input(key='usuario',size=(16, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*',size=(17, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de Login', layout)
#Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'adriana' and valores['senha'] == '123456':
            print('Bem vindo a Minha Interface!')
