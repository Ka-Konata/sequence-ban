# limite de 100 ids por comando
# slowmode de 20seg

from os        import curdir
from pyautogui import moveTo, click, press
from keyboard  import write
from datetime  import datetime
import crayons as cl

class Obj:
    def __init__(self, reason, ids, pos, times, per_time):
        self.reason   = reason
        self.ids      = ids
        self.pos      = pos
        self.times    = times
        self.per_time = per_time


    def ban(self, all_banned, count):
        '''Envia o comando de ban'''

        dat      = datetime.now()
        moment   = f'{dat.hour}:{dat.minute}:{dat.second}'

        # Criando a mensagem do comando com todos os ids
        msg   = f'>>ban '
        _list = self.ids[all_banned:all_banned + self.per_time]
        for atual in range(0, len(_list)):
            self.atual = atual
            msg += f'{_list[atual]} '
            print(cl.green(f'[{moment}] [{atual + 1}/{len(_list)}] id: {_list[atual]} adicionado ao comando atual [{count}/{self.times}]'))
        msg += f'{self.reason}'

        moveTo(self.pos)
        click()
        write(msg)
        press('enter')

    def enviar(self, msg):
        '''Envia uma mensagem'''

        moveTo(self.pos)
        click()
        write('[Vortex mode] ' + msg)
        press('enter')