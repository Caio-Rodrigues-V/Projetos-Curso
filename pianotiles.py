# quais são os passos manuais que devo transformar em código
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep


pyautogui.click(1452,444)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0,0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1332,498, (0,0,0)):
        click(1332,498)
    if pyautogui.pixelMatchesColor(1415,495, (0,0,0)):
        click(1415,495)
    if pyautogui.pixelMatchesColor(1487,495, (0,0,0)):
        click(1487,495)
    if pyautogui.pixelMatchesColor(1573,498, (0,0,0)):
        click(1573,498)