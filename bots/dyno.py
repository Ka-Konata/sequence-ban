# limite de 1 id por comando
# slowmode de 3seg

from os import curdir
from pyautogui import moveTo, click, press
from keyboard import write, wait, is_pressed

class Obj:
    def __init__(self, reason, ids, pos):
        self.reason = reason
        self.ids    = ids
        self.pos    = pos


    def ban(self, atual):
        '''Envia o comando de ban'''

        self.atual = atual
        moveTo(self.pos)
        click()
        write(f'?ban {self.ids[atual]} {self.reason}')
        press('enter')

    def enviar(self, msg):
        '''Envia uma mensagem'''

        moveTo(self.pos)
        click()
        write('[Dyno mode] ' + msg)
        press('enter')