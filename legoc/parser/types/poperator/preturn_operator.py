from legoc.parser.types.poperator.poperator import POperator


class PReturnOperator(POperator):
    def __init__(self, lexem):
        super(PReturnOperator, self).__init__(lexem)
        self.type_name = 'PReturnOperator'
        self.complete = True
