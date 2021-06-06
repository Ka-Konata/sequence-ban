# limite de 100 ids por comando
# slowmode de 20seg

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


    def ban(self, all_banned, per_time, count, times):
        '''Envia o comando de ban'''

        dat      = datetime.now()
        moment   = f'{dat.hour}:{dat.minute}:{dat.second}'

        # Criando a mensagem do comando com todos os ids
        msg = f'>>ban '
        for atual in range(0, self.ids[all_banned:all_banned + per_time]):
            msg += f'{self.ids[atual]}\n'
            print(cl.green(f'[{moment}] [{atual + 1}/{len(self.ids)}] id: {self.ids[atual]} adicionado ao comando atual [{count}/{times}]'))
        msg += f'\r {self.reason}'

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