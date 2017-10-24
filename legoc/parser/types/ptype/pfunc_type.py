from legoc.parser.types.ptype.pcomplex_type import PComplexType


class PFuncType(PComplexType):
    def __init__(self):
        super(PFuncType, self).__init__()
        self.type_name = 'PFuncType'
