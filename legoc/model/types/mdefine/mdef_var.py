from legoc.model.types.mdefine.mdef import MDef


class MDefVar(MDef):
    def __init__(self, modifiers, type, name):
        super(MDefVar, self).__init__()
        self.tstack.append(MDefVar.__name__)

        self.modifiers = modifiers
        self.type = type
        self.name = name
