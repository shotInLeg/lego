from legoc.parser.types.poperator.pcycle_operator import PCycleOperator


class PForOperator(PCycleOperator):
    def __init__(self, lexem):
        super(PForOperator, self).__init__(lexem)
        self.type_name = 'PForOperator'
        self.complete = True
