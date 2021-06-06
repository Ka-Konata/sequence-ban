# limite de 1 id por comando
# slowmode de 3seg

from os        import curdir
from pyautogui import moveTo, click, press
from keyboard  import write
from datetime  import datetime
import crayons as cl

class Obj:
    def __init__(self, reason, ids, pos):
        self.reason = reason
        self.ids    = ids
        self.pos    = pos


    def ban(self, atual):
        '''Envia o comando de ban'''

        dat      = datetime.now()
        moment   = f'{dat.hour}:{dat.minute}:{dat.second}'
        print(cl.green(f'[{moment}] [{atual + 1}/{len(self.ids)}] comando utilizado para o id: {self.ids[atual]}'))

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