from random import random
import PySimpleGUI as sg
import random
sg.theme('LightGray1')
a=random.randint(1,10)
b=random.randint(1,10)
soma=a+b
soma=str(soma)
a=str(a)
b=str(b)

layout = [
    [sg.Text('Vamos aprender somar?')],
    [sg.Text('Quanto é '+ a+" + "+b+" ??")],
    [sg.Input(key='palpite')],
    [sg.Button('Ok')],
    [sg.Text('',key= 'mensagem')],
    
]
window = sg.Window('Soma',layout=layout)
while (True):
    event, values = window.read()
    
    palpite_do_user = values['palpite']
   

    if palpite_do_user == soma:
            window['mensagem'].update('Parabéns, você acertou!')
            sg.Popup('Parabéns, você acertou!',image=(sg.EMOJI_BASE64_HAPPY_THUMBS_UP))
        
    elif palpite_do_user != soma:
            window['mensagem'].update('Que pena, tente novamente!')
            sg.Popup('Que pena, você errou não desista e tente novamente!', image=(sg.EMOJI_BASE64_FRUSTRATED))







