from legoc.parser.types.pvalue.pvalue import PValue


class PRValue(PValue):
    def __init__(self, lexem):
        super(PRValue, self).__init__(lexem)
        self.type_name = 'PRValue'
        self.complete = True

        self.type = None
