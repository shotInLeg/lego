from legoc.parser.types.ptype.ptype import PType


class PSimpleType(PType):
    def __init__(self):
        super(PSimpleType, self).__init__()
        self.type_name = 'PSimpleType'
