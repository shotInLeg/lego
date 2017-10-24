from legoc.parser.types.poperator.pcycle_operator import PCycleOperator


class PWhileOperator(PCycleOperator):
    def __init__(self, lexem):
        super(PWhileOperator, self).__init__(lexem)
        self.type_name = 'PWhileOperator'
        self.complete = True
