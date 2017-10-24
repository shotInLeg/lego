from legoc.parser.types.ptype.ptype import PType


class PComplexType(PType):
    def __init__(self):
        super(PComplexType, self).__init__()
        self.type_name = 'PComplexType'
