from legoc.parser.types.ptype.ptype import PType


class PTemplType(PType):
    def __init__(self, lexeme):
        super(PTemplType, self).__init__(lexeme)
        self.tstack.append(PTemplType.__name__)
        self.args = []

    def get(self):
        return self
