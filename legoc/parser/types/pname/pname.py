from legoc.parser.types.pvalue.prvalue import PRValue


class PName(PRValue):
    def __init__(self, lexem):
        super(PName, self).__init__(lexem)
        self.type_name = 'PName'
        self.complete = True
