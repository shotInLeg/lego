from legoc.parser.types.poperator.pcond_operator import PCondOperator


class PIfElifElseOperator(PCondOperator):
    def __init__(self, lexem):
        super(PIfElifElseOperator, self).__init__(lexem)
        self.type_name = 'PIfElifElseOperator'
        self.complete = True
