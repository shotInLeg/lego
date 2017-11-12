from legoc.parser.types.poperator.poperator import POperator


class PWith(POperator):
    def __init__(self, lexeme):
        super(PWith, self).__init__(lexeme)
        self.tstack.append(PWith.__name__)

    def get(self):
        return self
