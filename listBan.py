# -*- coding: utf-8 -*-

from bots import dyno, vortex
from cogs import setter
from cogs import utils
from cogs import default
import cogs.texts as txt

from keyboard  import is_pressed
from pyautogui import confirm
from datetime  import datetime
from math      import ceil
import crayons as cl
import time

class main(default.padrao):
    def __init__(self):
        super().__init__()


    def run(self):
        global ids

        utils.clear_screen()
        if self.first_time:
            resp = confirm(txt.msg_9, title='AVISO IMPORTANTE', buttons=['OK', 'NÃO MOSTRAR NOVAMENTE'])

            if resp == 'NÃO MOSTRAR NOVAMENTE':
                utils.first_time(self.configs)
                self.configs['first-time'] = False


        print(cl.green(txt.hello))
        utils.slow_print(txt.version)
        time.sleep(1)
        utils.clear_screen()

        print(cl.green(txt.msg_1))

        while True:
            try:
                mode = int(input('Sua escolha: '))
                if not 1 <= mode <= 6:
                    utils.clear_screen()
                    print(cl.red('Sua escolha não corresponde a nenhum modo existente'))
                    print(cl.green(txt.msg_1))
                else: utils.clear_screen(); break 
            except:
                utils.clear_screen()
                print(cl.red('Sua escolha não corresponde a nenhum modo existente'))
                print(cl.green(txt.msg_1))

        customized = True if mode == 2 or mode == 4 or mode == 5 else False
        if mode != 6: self.set_ids(self.path, customized=customized)

        if len(self.ids) > 0 or mode == 6:
            stoped  = False

            if 1 <= mode <= 2:
                if mode == 2:
                    self.set_pos()
                    self.set_reason()
                    self.set_ids('None', customized=customized)
                    self.set_slowmode_dyno()
                    self.ask_for_change()

                print(cl.green(txt.msg_2))
                for atual in range(0, len(self.ids)):
                    obj_dyno = dyno.Obj(self.reason, self.ids, self.pos)
                    choice   = obj_dyno
                    obj_dyno.ban(atual)

                    if utils.stop_request(obj_dyno): stoped=True; break
                    elif atual < len(self.ids) - 1: time.sleep(self.slowmode_dyno)

            elif 3 <= mode <= 4:
                if mode == 4:
                    self.set_pos()
                    self.set_reason()
                    self.set_ids('None', customized=customized)
                    self.set_slowmode_vortex()
                    self.ask_for_change()

                print(cl.green(txt.msg_2))
                per_time   = 5
                all_banned = 0
                times      = ceil(len(self.ids) / per_time)

                obj_vortex = vortex.Obj(self.reason, self.ids, self.pos, times, per_time)
                choice     = obj_vortex

                for count in range (0, times):
                    obj_vortex.ban(all_banned, count)
                    all_banned += per_time

                    if utils.stop_request(obj_vortex): stoped=True; break
                    elif count < len(self.ids) - 1: time.sleep(self.slowmode_vortex)

            elif mode == 5:
                stoped=True

                self.set_pos()
                self.set_reason()
                self.set_ids('None', customized=customized)
                self.set_slowmode_dyno()
                self.set_slowmode_vortex()
                self.ask_for_change()

            elif mode == 6:
                quit()

            if not stoped:
                choice.enviar(f'-- Todos os comandos enviados | ids [{len(self.ids)}/{len(self.ids)}]')
                print(cl.green('\n' + '-'*55))
                print(cl.green('Lista completa.\n'))

        print(cl.green('\n--------------- ENTER para voltar para o menu | ESC para fechar ---------------'))


# Iniciando o programa
if __name__ == '__main__':
    main().run()

    while True:
        if is_pressed('esc'):
            utils.clear_screen()
            quit()

        if is_pressed('enter'):
            main().run()
