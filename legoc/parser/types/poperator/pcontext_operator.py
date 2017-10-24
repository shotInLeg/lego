from legoc.parser.types.poperator.poperator import POperator


class PContextOperator(POperator):
    def __init__(self, lexem):
        super(PContextOperator, self).__init__(lexem)
        self.type_name = 'PContextOperator'
        self.complete = True
