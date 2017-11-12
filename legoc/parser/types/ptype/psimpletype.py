from legoc.parser.types.ptype.ptype import PType


class PSimpleType(PType):
    def __init__(self, lexeme):
        super(PSimpleType, self).__init__(lexeme)
        self.tstack.append(PSimpleType.__name__)

    def get(self):
        return self
