from legoc.parser.types.ptype.ptype import PType


class PSimpleType(PType):
    def __init__(self, lexem):
        super(PSimpleType, self).__init__(lexem)
        self.type_name = 'PSimpleType'
