from legoc.parser.types.poperator.pcycle_operator import PCycleOperator


class PDoWhileOperator(PCycleOperator):
    def __init__(self, lexem):
        super(PDoWhileOperator, self).__init__(lexem)
        self.type_name = 'PDoWhileOperator'
        self.complete = True
