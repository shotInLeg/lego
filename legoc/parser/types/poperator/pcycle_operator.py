from legoc.parser.types.poperator.poperator import POperator


class PCycleOperator(POperator):
    def __init__(self, lexem):
        super(PCycleOperator, self).__init__(lexem)
        self.type_name = 'PCycleOperator'
        self.complete = True
