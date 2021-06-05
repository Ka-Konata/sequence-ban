from keyboard  import is_pressed
import crayons as cl
import time

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

    if is_pressed('delete'):
        obj.enviar(f'-- Processo interrompido [{obj.atual + 1}/{len(obj.ids)}]')
        print(cl.red(f'''
Programa interrompido com DELETE 
Status atual: {0 if len(obj.ids) == 0 else obj.atual + 1} comandos utilizados de {len(obj.ids)} 
Ultimo id: {obj.ids[obj.atual]}'''))
        return True
    else: return False