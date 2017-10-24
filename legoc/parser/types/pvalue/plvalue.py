from legoc.parser.types.pvalue.pvalue import PValue


class PLValue(PValue):
    def __init__(self, lexem):
        super(PLValue, self).__init__(lexem)
        self.type_name = 'PLValue'
        self.complete = True
