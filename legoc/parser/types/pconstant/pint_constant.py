from legoc.parser.types.pconstant.pconstant import PConstant


class PIntConstant(PConstant):
    def __init__(self, lexem):
        super(PIntConstant, self).__init__(lexem)
        self.type_name = 'PIntConstant'
        self.complete = True
