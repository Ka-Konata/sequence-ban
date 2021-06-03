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

from pyautogui import *
from crayons import *
from datetime import datetime
from pynput import keyboard
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
    
def open_ids(path):
    """Abre o arquico txt contendo os ids"""

    global run, ids

    try: 
        arquiv = open(path, "r")

        for line in arquiv:
            ids.append(line[:18])

        arquiv.close()

        print(green(f"arquivo aberto com sucesso! ({len(ids)} linhas)"))
        return True
    except FileNotFoundError:
        print(red(f"Não foi possível abrir o arquivo {path}"))
        return False

def enviar(msg):
    """Envia uma mensagem"""

    moveTo(pos)
    click()
    write(msg)
    keyDown("enter")
    keyUp("enter")

if __name__ == "__main__":
    print(green(hello))
    pos = tela()
    reason = input("reason dos bans: ")
    path   = input("path do arquivo contendo os id's a serem banidos: ")
    print(green("-"*55))
    print(green("\nIniciando o processo.."))

    # Procurando pelos ids
    if open_ids(path):
        print(green("\nMantenha a tecla ESC pressionada para interromper"))
        print(green("Começando a enviar os comandos\n"))

        for atual in range(0, len(ids)):

            # Banindo o id
            enviar(f"?ban {ids[atual]} {reason}")

            dat = datetime.now()
            moment = f"{dat.hour}:{dat.minute}:{dat.second}"

            print(green(f"[{moment}] [{atual}/{len(ids)}] comando utilizado para o id: {ids[atual]}"))
            time.sleep(4)
            
            # Verificando se o usuário quer interromper os comandos
            with keyboard.Events() as events:
                event = events.get(1.0)
            if event and event.key == keyboard.Key.esc:
                enviar(f"-- Processo interrompido [{atual + 1}/{len(ids)}]")
                print(red(f"""\nPrograma interrompido com ESC \nStatus atual: {0 if len(ids) == 0 else atual + 1} comandos utilizados de {len(ids)} \nUltimo id: {ids[atual]}"""))
                break

            if atual + 1 == len(ids):
                enviar(f"-- Todos os comandos enviados [{atual}/{len(ids)}]")
                print(green("\n" + "-"*55))
                print(green("Lista completa.\n"))


# Para o script não encerrar após o uso:
while True:
    input("\n------ press ENTER to close ------")
    break
