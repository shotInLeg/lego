from legoc.parser.types.pvalue.plvalue import PLValue


class PConstant(PLValue):
    def __init__(self, lexem):
        super(PConstant, self).__init__(lexem)
        self.type_name = 'PConstant'
        self.complete = True
