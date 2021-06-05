# limite de 100 ids por comando
# slowmode de 20seg

class Obj:
    def __init__(self, reason, ids, pos):
        self.reason = reason
        self.ids    = ids
        self.pos    = pos


    def ban(self):
        pass