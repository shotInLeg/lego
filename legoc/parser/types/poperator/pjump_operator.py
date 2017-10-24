from legoc.parser.types.poperator.poperator import POperator


class PJumpOperator(POperator):
    def __init__(self, lexem):
        super(PJumpOperator, self).__init__(lexem)
        self.type_name = 'PJumpOperator'
        self.complete = True
