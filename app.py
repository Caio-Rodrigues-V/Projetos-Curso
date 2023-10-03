#entender como funciona o bot - passos manuais


# 1 -  reconhecer cada teclado do jogo (posso usar cores rgb )

# 2 - achar um jeito de quando a tecla do jogo passar encima da tecla de botoes ele acionar a tecla e pontuar

import pyautogui as py
import keyboard as ky
from time import sleep


while ky.is_pressed('1') == False:

    if py.pixelMatchesColor(811,793,(0,152,0)):
        py.press('a')
    

    if py.pixelMatchesColor(878,793,(255,0,0)):
        py.press('s')
    

    if py.pixelMatchesColor(970,794,(244,244,2)):
        py.press('j')
