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
                                        ██                  ████\n\n"""


from pyautogui import moveTo, click, press
from keyboard import write, wait, is_pressed
from crayons import *
from datetime import datetime
import time

ids = list()
pos = None

def tela():
    """Pede a posição da tela em que a caixa de texto se encontra, ou seta como padrão"""

    print(green("-"*55 + '\nCite a posição da tela (em pixels) na qual se encontra \na caixa de texto do discord ex: 700 e 950 \nDigite "padrão/p" para pular (posição padrão: x50 e y962)\n'))

    pos_x = input("posição x: ")
    if pos_x in "padrão/padrao/p/P":
        pos = (50, 962)
        print(yellow("-- [AVISO] Utilizando a posição definida por padrão \n") + green("-"*55))
        return pos

    pos_y = input("posição y: ")
    if pos_y in "padrão/padrao/p/P":
        pos = (50, 962)
        print(yellow("-- [AVISO] Utilizando a posição definida por padrão \n") + green("-"*55))
        return pos

    pos = (int(pos_x), int(pos_y))
    print(green("-"*55))
    return pos
    
def open_ids():
    """Abre o arquico txt contendo os ids"""

    global ids

    def f_open(f):
        arquiv = open(f, "r")
        for line in arquiv:
            ids.append(line[:18])
        arquiv.close()
        print(green(f"arquivo aberto com sucesso! ({len(ids)} linhas)"))

    try: 
        path = "ids.txt"
        f_open(path)
        return True
    except FileNotFoundError:
        try: 
            print(red("O arquivo ids.txt padrão não foi encontrado"))
            path = input("Caminho do arquivo contendo os ids a ser usado: ")
            f_open(path)
            return True
        except FileNotFoundError:
            print(red(f"Não foi possível abrir o arquivo {path}"))
            return False

def enviar(msg):
    """Envia uma mensagem"""

    moveTo(pos)
    click()
    write(msg)
    press("enter")

if __name__ == "__main__":
    print(green(hello))
    pos    = tela()
    reason = input("reason dos bans: ")
    run    = open_ids()

    # Procurando pelos ids
    if run:
        print(green("-"*55))
        print(green("\nIniciando o processo.."))
        print(green("\nMantenha a tecla ESC pressionada para interromper"))
        print(green("Começando a enviar os comandos\n"))

        for atual in range(0, len(ids)):

            # Banindo o id
            enviar(f"?ban {ids[atual]} {reason}")

            dat = datetime.now()
            moment = f"{dat.hour}:{dat.minute}:{dat.second}"

            print(green(f"[{moment}] [{atual + 1}/{len(ids)}] comando utilizado para o id: {ids[atual]}"))
            time.sleep(4)
            
            # Verificando se o usuário quer interromper os comandos
            if is_pressed('esc'):
                enviar(f"-- Processo interrompido [{atual + 1}/{len(ids)}]")
                print(red(f"""\nPrograma interrompido com ESC \nStatus atual: {0 if len(ids) == 0 else atual + 1} comandos utilizados de {len(ids)} \nUltimo id: {ids[atual]}"""))
                break

            if atual + 1 == len(ids):
                enviar(f"-- Todos os comandos enviados [{atual + 1}/{len(ids)}]")
                print(green("\n" + "-"*55))
                print(green("Lista completa.\n"))


# Para o script não encerrar após o uso:
while True:
    print(green("\n----------------- press ENTER to close ----------------"))
    wait("enter")
    break
