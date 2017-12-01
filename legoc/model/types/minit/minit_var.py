from legoc.model.types.minit.minit import MInit


class MInitVar(MDef):
    def __init__(self, name, exp):
        super(MInitVar, self).__init__()
        self.tstack.append(MInitVar.__name__)

        self.name = name
        self.exp = exp
