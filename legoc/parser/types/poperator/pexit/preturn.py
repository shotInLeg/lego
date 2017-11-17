from legoc.parser.types.poperator.poperator import POperator


class PReturn(POperator):
    def __init__(self, child=None):
        super(PReturn, self).__init__('return')
        self.tstack.append(PReturn.__name__)

        self.child = child

    def get(self):
        return self

    def __str__(self):
        return '{{return {}}}'.format(
            self.child
        )
