from legoc.parser.types.pvalue.prvalue import PRValue


class PConstant(PRValue):
    def __init__(self, lexem):
        super(PConstant, self).__init__(lexem)
        self.type_name = 'PConstant'
        self.complete = True

        self.type = None
