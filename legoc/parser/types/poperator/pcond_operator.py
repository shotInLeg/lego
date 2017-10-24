from legoc.parser.types.poperator.poperator import POperator


class PCondOperator(POperator):
    def __init__(self, lexem):
        super(PCondOperator, self).__init__(lexem)
        self.type_name = 'PCondOperator'
        self.complete = True
