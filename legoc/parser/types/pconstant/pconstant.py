from legoc.parser.types.pvalue.prvalue import PRValue


class PConstant(PRValue):
    def __init__(self, lexeme):
        super(PConstant, self).__init__()
        self.tstack.append(PConstant.__name__)
        self.str_value = lexeme

    def get(self):
        return self
