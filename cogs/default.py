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
                'pos': [50, 962],
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