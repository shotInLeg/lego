from legoc.parser.types.ptype.ptype import PType


class PComplexType(PType):
    def __init__(self,lexem):
        super(PComplexType, self).__init__(lexem)
        self.type_name = 'PComplexType'
