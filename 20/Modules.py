class Module:
    def __init__(self, id, destination_modules):
        self.id = id
        self.destination_modules = destination_modules

class FlipFlop(Module):
    def __init__(self, id, destination_modules):
        super().__init__(id, destination_modules)
        self.switch = 0
    def flip(self):
        if self.switch == 0:
            self.switch = 1
        else:
            self.switch = 0

class Conjunction(Module):
    def __init__(self, id, destination_modules):
        super().__init__(id, destination_modules)
        self.memory = {}