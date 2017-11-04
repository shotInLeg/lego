from legoc.parser.types.ptype.pcomplex_type import PComplexType


class PFuncType(PComplexType):
    def __init__(self, lexem):
        super(PFuncType, self).__init__(lexem)
        self.type_name = 'PFuncType'
