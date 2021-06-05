
from cogs      import texts as txt
from cogs      import utils
from pyautogui import position
from keyboard  import is_pressed
import crayons as cl
import time

def set_postion(default_position):
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


def open_ids(path, customized=False):
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
                if not customized: print(cl.red('O arquivo ids.txt padrão não foi encontrado'))
                print(cl.green(txt.msg_3))
                path = str(input('path: '))
                if path in 'padrão/padrao/p': path = 'ids.txt'
                utils.clear_screen()
                ids = f_open(path)
                return ids
            except FileNotFoundError:
                print(cl.red(f'Não foi possível abrir o arquivo {path}'))