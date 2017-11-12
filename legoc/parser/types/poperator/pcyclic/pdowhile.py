from legoc.parser.types.poperator.poperator import POperator


class PDoWhile(POperator):
    def __init__(self, lexeme):
        super(PDoWhile, self).__init__(lexeme)
        self.tstack.append(PDoWhile.__name__)

    def get(self):
        return self
