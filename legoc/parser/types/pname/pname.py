from legoc.parser.types.pvalue.plvalue import PLValue


class PName(PLValue):
    def __init__(self, lexem):
        super(PName, self).__init__(lexem)
        self.type_name = 'PName'
        self.complete = True
