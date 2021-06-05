# -*- coding: utf-8 -*-

hello = """███  ██
███ ███    ███   ██████    ████  █████  ████
██████   ███ ███ ███  ██  ██  ██  ███  ██  ███
██████   ██  ███ ███  ██     ███  ███     ████
███ ███  ██  ███ ███  ██  ██  ██  ███  ███ ███          ███                        ███
███  ██  ██████  ███  ██  ██ ███  ███  ███ ███ ███      ███                        ███
                                     █         ███      ███                       ████
              ██████████████████████████ ███   ███      ███      █     ████████████████████████████
              ██████████████████████████ ███   ███      ███  ██████            ████
                                         ███   ███████  ███████                ████
                                         ███   ███      ████                   ████████████████
                                         ███   ███      ███                   █████████████████
                                         ███   ███      ███                   ████          ███
                                         ███   ███      ███                  ████           ███
                                         ███   ███      ███      ███        ████            ███
                                         ███   ███      ███      ███       ████            ████
                                         ███   ███████  ███     ████     ████             ████
                                       ███████████████  ███████████    ████         █████████
                                        ██                  ████"""

version = 'Sequence Ban - v2.0 (pre-release)'

msg_1 = '''----------- Escolha o modo que deseja usar ------------
Digite o número correspondente a sua scolha
[1] - Dyno (padrão)
[2] - Dyno (customizado)
[3] - Vortex (padrão) [indisponível]
[4] - Vortex (customizado) [indisponível]
[5] - Atualizar as configurações de preferência [indisponível]'''

msg_2 = '''-------------------------------------------------------
Iniciando o processo..
\nMantenha a tecla ESC pressionada para interromper
Começando a enviar os comandos\n'''

msg_3 = '''-------------------------------------------------------
Digite o caminho para o arquivo txt contendo os ids
Ou apenas digite padrão/p para usar o padrão
'''

msg_4 = '''-------------------------------------------------------
Posicione o mouse sobre a caixa de texto do discord
Aoós posicionado, tecle DELETE para confirmar

tecle P ou S para usar a posição padrão
tecle ESPACE para digitar você mesmo a posição em pixels'''

msg_5 = '''-------------------------------------------------------
Digite a posição em que a caixa de mensgem do discord se encontra \n'''

msg_6 = '''-------------------------------------------------------
Digite o intervalo de tempo a mais entre cada ban
ex: 2.4'''


from pyautogui import position
from keyboard import wait, is_pressed
import crayons as cl
import time
from datetime import datetime
from bots import dyno, vortex

ids = list()


def set_postion(default_position):
    '''Pede a posição da tela em que a caixa de texto se encontra, ou seta como padrão'''

    print(cl.green(msg_4))
    while True:
        if is_pressed('delete'):
            pos = position()
            return (pos.x, pos.y)

        if is_pressed('p') or is_pressed('s'):
            return default_position

        if is_pressed('space'):
            clear_screen()
            while True:
                try: 
                    print(cl.green(msg_5))
                    pos_x = int(input('posição x: '))
                    pos_y = int(input('posição y: '))
                    pos = (pos_x, pos_y)
                    return pos
                except ValueError:
                    clear_screen()
                    print(cl.red('Posição inválida'))


def open_ids(path, customized=False):
    '''Abre o arquivo txt contendo os ids'''

    def f_open(f):
        global ids

        ids = list()
        arquiv = open(f, 'r')
        for line in arquiv:
            ids.append(line[:18])
        arquiv.close()
        clear_screen()

    while True:
        try: 
            f_open(path)
            return path
        except FileNotFoundError:
            try: 
                if not customized: print(cl.red('O arquivo ids.txt padrão não foi encontrado'))
                print(cl.green(msg_3))
                path = str(input('path: '))
                if path in 'padrão/padrao/p': path = 'ids.txt'
                clear_screen()
                f_open(path)
                return path
            except FileNotFoundError:
                print(cl.red(f'Não foi possível abrir o arquivo {path}'))


def slow_print(text, timer=0.05):
    '''Printa letra por letra'''

    for l in text: 
        print(cl.green(l), end='')
        time.sleep(timer)
    print('')


def clear_screen():
    '''Limpa a tela'''
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def stop_request(obj):
    '''Detecta um clique do teclado que para o processo de banimento'''

    if is_pressed('esc'):
        obj.enviar(f'-- Processo interrompido [{obj.atual + 1}/{len(obj.ids)}]')
        print(cl.red(f'''
Programa interrompido com ESC 
Status atual: {0 if len(obj.ids) == 0 else obj.atual + 1} comandos utilizados de {len(obj.ids)} 
Ultimo id: {obj.ids[obj.atual]}'''))
        return True
    else: return False


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
        print(cl.green(hello))
        slow_print(version)
        time.sleep(1)
        clear_screen()

        print(cl.green(msg_1))

        while True:
            try:
                mode = int(input('Sua escolha: '))
                if not 1 <= mode <= 5:
                    clear_screen()
                    print(cl.red('Sua escolha não corresponde a nenhum modo existente'))
                    print(cl.green(msg_1))
                else: clear_screen(); break 
            except:
                clear_screen()
                print(cl.red('Sua escolha não corresponde a nenhum modo existente'))
                print(cl.green(msg_1))

        customized = True if mode == 2 or mode == 4 else False
        if open_ids(self.path, customized=customized):
            obj_dyno   = dyno.Obj(self.reason, ids, self.pos)
            obj_vortex = vortex.Obj(self.reason, ids, self.pos)
            choice  = obj_dyno if 1 <= mode <= 2 else obj_vortex
            stoped  = False

            if mode == 1:
                print(cl.green(msg_2))
                for atual in range(0, len(ids)):
                    obj_dyno.ban(atual)
                    dat = datetime.now()
                    moment = f'{dat.hour}:{dat.minute}:{dat.second}'
                    print(cl.green(f'[{moment}] [{atual + 1}/{len(ids)}] comando utilizado para o id: {ids[atual]}'))
                    if stop_request(obj_dyno): stoped=True; break
                    elif atual < len(ids) - 1: time.sleep(self.slowmode_dyno)

            elif mode == 2:
                self.pos = set_postion(self.pos)
                clear_screen()

                print(cl.green('-'*55))
                self.reason = str(input('Digite a reason dos bans: '))
                clear_screen()
                
                self.path = open_ids('None', customized=True)
                
                while True:
                    try:
                        print(cl.green(msg_6))
                        self.slowmode_dyno = float(input('Segundos: '))
                        break
                    except:
                        clear_screen()
                        print(cl.red('tempo inválido'))
                clear_screen()

                print(cl.green(msg_2))
                for atual in range(0, len(ids)):
                    obj_dyno.ban(atual, customized=True, pos=self.pos)
                    dat = datetime.now()
                    moment = f'{dat.hour}:{dat.minute}:{dat.second}'
                    print(cl.green(f'[{moment}] [{atual + 1}/{len(ids)}] comando utilizado para o id: {ids[atual]}'))
                    if stop_request(obj_dyno): stoped=True; break
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
