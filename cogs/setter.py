
from cogs      import texts as txt
from cogs      import utils
from pyautogui import position
from keyboard  import is_pressed
import crayons as cl
import time

def setter_reason(default_reason):
    print(cl.green(txt.msg_7))
    reason = str(input('reason: '))

    if reason in 'padrão/padrao/p':
        reason = default_reason
        
    return reason


def setter_path(default_path):
    print(cl.green(txt.msg_3))
    path = str(input('path: '))

    if path in 'padrão/padrao/p': 
        path = default_path

    return path


def setter_slowmode(default_slow, bot):
    while True:
        try:
            print(cl.green(txt.msg_6))
            slow = input(f'Segundos [{bot}]: ')

            if slow in 'padrão/padrao/p':
                slow = default_slow
            else:
                slow = float(slow)

            break
        except:
            utils.clear_screen()
            print(cl.red('tempo inválido'))

    return slow


def setter_postion(default_position):
    '''Pede a posição da tela em que a caixa de texto se encontra, ou seta como padrão'''

    print(cl.green(txt.msg_4))
    while True:
        if is_pressed('delete'):
            pos = position()
            return (pos.x, pos.y)

        if is_pressed('p') or is_pressed('s'):
            return default_position

        if is_pressed('space'):
            utils.clear_screen()
            while True:
                try: 
                    print(cl.green(txt.msg_5))
                    pos_x = int(input('posição x: '))
                    pos_y = int(input('posição y: '))
                    pos = (pos_x, pos_y)
                    return pos
                except ValueError:
                    utils.clear_screen()
                    print(cl.red('Posição inválida'))


def setter_ids(path, customized=False, padrao='ids.txt'):
    '''Abre o arquivo txt contendo os ids'''

    def f_open(f):
        ids = list()
        arquiv = open(f, 'r')
        for line in arquiv:
            ids.append(line[:18])
        arquiv.close()
        utils.clear_screen()
        return ids

    while True:
        try: 
            ids = f_open(path)
            return ids
        except FileNotFoundError:
            try: 
                if not customized: 
                    print(cl.red(f'O arquivo {padrao} padrão não foi encontrado'))

                path = setter_path(padrao)
                utils.clear_screen()

                ids  = f_open(path)
                return ids
            except FileNotFoundError:
                print(cl.red(f'Não foi possível abrir o arquivo {path}'))