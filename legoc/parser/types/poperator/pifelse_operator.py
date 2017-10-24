from legoc.parser.types.poperator.pcond_operator import PCondOperator


class PIfElseOperator(PCondOperator):
    def __init__(self, lexem):
        super(PIfElseOperator, self).__init__(lexem)
        self.type_name = 'PIfElseOperator'
        self.complete = True
