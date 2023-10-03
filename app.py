""" Quais passos devo seguir para enviar uma msg para uma pessoa no wpp?

1 - achar a pessoa na lista de contato

2 - enviar individualmente uma mensagem para cada pessoa

3 - pausar entre cada envio
 ----------------------------------------------------------------------------------

1 - escolher um contato

2 - enviar mensagem para este contato

3 - repetir isso para outro contato """


""" import webbrowser as wb
import pyautogui as py
from time import sleep

telefones = [5521984354821,553196402751,5521965605687]

for telefone in telefones:
    wb.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    iniciar = py.locateCenterOnScreen('inciar_conversa.png',confidence=0.9)
    py.click(iniciar[0],iniciar[1])
    sleep(10)
    web = py.locateCenterOnScreen('web.png',confidence=0.9)
    py.click(web[0],web[1])
    py.typewrite("ASDAD")
    py.press('enter')
    sleep(200) """


import webbrowser as wb
import pyautogui as py
from time import sleep

telefones = []
with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

for telefone in telefones:
    wb.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    iniciar = py.locateCenterOnScreen('inciar_conversa.png',confidence=0.9)
    py.click(iniciar[0],iniciar[1])
    sleep(10)
    web = py.locateCenterOnScreen('web.png',confidence=0.9)
    py.click(web[0],web[1])
    sleep(15)
    py.typewrite("Olá ! !")
    py.press('enter')
    sleep(200)