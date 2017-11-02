from legoc.parser.types.pconstant.pconstant import PConstant
from legoc.parser.types.ptype.psimple_type import PSimpleType


class PDblConstant(PConstant):
    def __init__(self, lexem):
        super(PDblConstant, self).__init__(lexem)
        self.type_name = 'PDblConstant'
        self.complete = True

        self.type = PSimpleType('Dbl')
