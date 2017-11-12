from legoc.parser.types.poperator.poperator import POperator


class PIf(POperator):
    def __init__(self, lexeme):
        super(PIf, self).__init__(lexeme)
        self.tstack.append(PIf.__name__)

    def get(self):
        return self
