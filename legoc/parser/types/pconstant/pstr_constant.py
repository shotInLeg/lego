from legoc.parser.types.pconstant.pconstant import PConstant


class PStrConstant(PConstant):
    def __init__(self, lexem):
        super(PStrConstant, self).__init__(lexem)
        self.type_name = 'PStrConstant'
        self.complete = True
