from cogs import setter
from cogs import utils
import json

class padrao:

    def __init__(self):
        '''Define os valores padrão'''

        self.pre_configs = {
            'reason': 'selfbot/raid [sequence-ban used]',
            'pos': [50, 962],
            'path': 'ids.txt',
            'slowmode-dyno': 4,
            'slowmode-vortex': 20
        }

        try:
            with open('configs.json', 'r', encoding='utf-8') as f:
                self.configs = json.load(f)
                f.close()
        except FileNotFoundError:
            self.configs = self.pre_configs
            with open('configs.json', 'w', encoding='utf-8') as f:
                default = json.dump(self.configs, f, indent=4)
                f.close()

        self.pos             = self.configs['pos']
        self.reason          = self.configs['reason']
        self.path            = self.configs['path']
        self.slowmode_dyno   = self.configs['slowmode-dyno']
        self.slowmode_vortex = self.configs['slowmode-vortex']
        self.ids             = list()


    def mode_5(self):
        pass


    def ask_for_change(self):
        from cogs import texts as txt
        import crayons as cl
        while True:
            print(cl.green(txt.msg_8))
            ask = str(input('salvar? '))
            if ask in 'sim/s':
                self.save_changes()
                break
            elif ask == 'default':
                self.save_changes(self.pre_configs)
                break
            elif ask in 'nao/n':
                break
            else:
                print(cl.red('Resposta não condiz com o esperado (sim ou nao)'))


    def save_changes(self, default=None):
        if default != None:
            new_configs = default
        else:
            new_configs = {
                'reason': self.reason,
                'pos': self.pos,
                'path': self.path,
                'slowmode-dyno': self.slowmode_dyno,
                'slowmode-vortex': self.slowmode_vortex
            }

        with open('configs.json', 'w', encoding='utf-8') as f:
            default = json.dump(new_configs, f, indent=4)
            f.close()


    def set_pos(self):
        self.pos = setter.setter_postion(self.pos)
        utils.clear_screen()

    def set_reason(self):
        self.reason = setter.setter_reason(self.reason)
        utils.clear_screen()


    def set_path(self):
        self.path = setter.setter_path(self.path)
        utils.clear_screen()


    def set_slowmode_dyno(self):
        self.slowmode_dyno = setter.setter_slowmode(self.slowmode_dyno, 'DYNO')
        utils.clear_screen()


    def set_slowmode_vortex(self):
        self.slowmode_vortex = setter.setter_slowmode(self.slowmode_vortex, 'VORTEX')
        utils.clear_screen()


    def set_ids(self, path, customized):
        self.ids = setter.setter_ids(path, customized=customized, padrao=self.path)
        utils.clear_screen()