from legoc.parser.types.poperator.poperator import POperator


class PFor(POperator):
    def __init__(self, lexeme):
        super(PFor, self).__init__(lexeme)
        self.tstack.append(PFor.__name__)

    def get(self):
        return self
