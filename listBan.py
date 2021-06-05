# -*- coding: utf-8 -*-

from bots import dyno, vortex
from cogs import setter
from cogs import utils
import cogs.texts as txt

from keyboard  import wait, is_pressed
from datetime  import datetime
import crayons as cl
import time

ids = list()

class padrao:
    def __init__(self):
        '''Define os valores padrão'''

        import json
        try:
            with open('confgs.json', 'r', encoding='utf-8') as f:
                configs = json.load(f)
                f.close()
        except FileNotFoundError:
            configs = {
                'reason': 'selfbot/raid [sequence-ban used]',
                'pos': [50, 700],
                'path': 'ids.txt',
                'slowmode-dyno': 4,
                'slowmode-vortex': 20
            }
            with open('confgsaa.json', 'w', encoding='utf-8') as f:
                default = json.dump(configs, f, indent=4)
                f.close()

        self.pos             = configs['pos']
        self.reason          = configs['reason']
        self.path            = configs['path']
        self.slowmode_dyno   = configs['slowmode-dyno']
        self.slowmode_vortex = configs['slowmode-vortex']


class main(padrao):
    def __init__(self):
        super().__init__()


    def run(self):
        print(cl.green(txt.hello))
        utils.slow_print(txt.version)
        time.sleep(1)
        utils.clear_screen()

        print(cl.green(txt.msg_1))

        while True:
            try:
                mode = int(input('Sua escolha: '))
                if not 1 <= mode <= 5:
                    utils.clear_screen()
                    print(cl.red('Sua escolha não corresponde a nenhum modo existente'))
                    print(cl.green(txt.msg_1))
                else: utils.clear_screen(); break 
            except:
                utils.clear_screen()
                print(cl.red('Sua escolha não corresponde a nenhum modo existente'))
                print(cl.green(txt.msg_1))

        customized = True if mode == 2 or mode == 4 else False
        ids        = setter.open_ids(self.path, customized=customized)
        if len(ids) > 0:
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

            if not stoped:
                choice.enviar(f'-- Todos os comandos enviados [{len(ids)}/{len(ids)}]')
                print(cl.green('\n' + '-'*55))
                print(cl.green('Lista completa.\n'))


# Iniciando o programa
if __name__ == '__main__':
    main().run()

# Para o script não encerrar após o uso:
while True:
    print(cl.green('\n----------------- press ENTER to close ----------------'))
    wait('enter')
    break
