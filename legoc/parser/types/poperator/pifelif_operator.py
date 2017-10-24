from legoc.parser.types.poperator.pcond_operator import PCondOperator


class PIfElifOperator(PCondOperator):
    def __init__(self, lexem):
        super(PIfElifOperator, self).__init__(lexem)
        self.type_name = 'PIfElifOperator'
        self.complete = True
