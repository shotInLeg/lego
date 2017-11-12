from legoc.parser.types.poperator.poperator import POperator


class PWhile(POperator):
    def __init__(self, lexeme):
        super(PWhile, self).__init__(lexeme)
        self.tstack.append(PWhile.__name__)

    def get(self):
        return self
