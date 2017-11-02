from legoc.parser.types.pconstant.pconstant import PConstant
from legoc.parser.types.ptype.psimple_type import PSimpleType

class PIntConstant(PConstant):
    def __init__(self, lexem):
        super(PIntConstant, self).__init__(lexem)
        self.type_name = 'PIntConstant'
        self.complete = True

        self.type = PSimpleType('Int')