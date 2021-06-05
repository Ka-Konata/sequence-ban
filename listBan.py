# -*- coding: utf-8 -*-

from bots import dyno, vortex
from cogs import setter
from cogs import utils
from cogs import default
import cogs.texts as txt

from keyboard  import wait, is_pressed
from datetime  import datetime
import crayons as cl
import time

ids = list()

class main(default.padrao):
    def __init__(self):
        super().__init__()


    def run(self):
        global ids

        utils.clear_screen()
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

        customized = True if mode == 2 or mode == 4 else False
        if mode != 6: ids = setter.open_ids(self.path, customized=customized, padrao=self.path)

        if len(ids) > 0 or mode == 6:
            obj_vortex = vortex.Obj(self.reason, ids, self.pos)
            stoped  = False

            if mode == 1:
                print(cl.green(txt.msg_2))
                for atual in range(0, len(ids)):
                    obj_dyno = dyno.Obj(self.reason, ids, self.pos)
                    choice   = obj_dyno
                    dat      = datetime.now()
                    moment   = f'{dat.hour}:{dat.minute}:{dat.second}'

                    obj_dyno.ban(atual)
                    print(cl.green(f'[{moment}] [{atual + 1}/{len(ids)}] comando utilizado para o id: {ids[atual]}'))
                    if utils.stop_request(obj_dyno): stoped=True; break
                    elif atual < len(ids) - 1: time.sleep(self.slowmode_dyno)

            elif mode == 2:
                self.pos = setter.set_postion(self.pos)
                utils.clear_screen()

                print(cl.green('-'*55))
                self.reason = str(input('Digite a reason dos bans: '))
                utils.clear_screen()
                
                ids = setter.open_ids('None', customized=True)
                
                while True:
                    try:
                        print(cl.green(txt.msg_6))
                        self.slowmode_dyno = float(input('Segundos: '))
                        break
                    except:
                        utils.clear_screen()
                        print(cl.red('tempo inválido'))
                utils.clear_screen()

                print(cl.green(txt.msg_2))
                for atual in range(0, len(ids)):
                    obj_dyno = dyno.Obj(self.reason, ids, self.pos)
                    choice   = obj_dyno
                    obj_dyno.ban(atual)
                    dat = datetime.now()
                    moment = f'{dat.hour}:{dat.minute}:{dat.second}'
                    print(cl.green(f'[{moment}] [{atual + 1}/{len(ids)}] comando utilizado para o id: {ids[atual]}'))
                    if utils.stop_request(obj_dyno): stoped=True; break
                    elif atual < len(ids) - 1: time.sleep(self.slowmode_dyno)

            elif mode == 3:
                print(cl.red('[ERROR] - Modo 3, vortex (padrão) ainda não funciona nesta versão'))
                stoped=True
            elif mode == 4:
                print(cl.red('[ERROR] - Modo 4, vortex (custoizado) ainda não funciona nesta versão'))
                stoped=True
            elif mode == 5:
                print(cl.red('[ERROR] - Modo 5, atualizar as configurações de preferência ainda não funciona nesta versão'))
                stoped=True

            elif mode == 6:
                quit()

            if not stoped:
                choice.enviar(f'-- Todos os comandos enviados [{len(ids)}/{len(ids)}]')
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
