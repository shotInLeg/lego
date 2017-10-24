from legoc.parser.types.pconstant.pconstant import PConstant


class PDblConstant(PConstant):
    def __init__(self, lexem):
        super(PDblConstant, self).__init__(lexem)
        self.type_name = 'PDblConstant'
        self.complete = True
