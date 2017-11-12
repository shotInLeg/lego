from legoc.parser.types.ptype.ptype import PType


class PFuncType(PType):
    def __init__(self, lexeme):
        super(PFuncType, self).__init__(lexeme)
        self.tstack.append(PFuncType.__name__)
        self.args = []

    def get(self):
        return self
