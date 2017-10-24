from legoc.parser.types.poperator.pcond_operator import PCondOperator


class PIfOperator(PCondOperator):
    def __init__(self, lexem):
        super(PIfOperator, self).__init__(lexem)
        self.type_name = 'PIfOperator'
        self.complete = True
