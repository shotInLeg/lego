from legoc.parser.types.poperator.poperator import POperator


class PForEach(POperator):
    def __init__(self, exp=None, context=None):
        super(PForEach, self).__init__('foreach')
        self.tstack.append(PForEach.__name__)

        self.exp = exp
        self.context = context

    def get(self):
        return self

    def __str__(self):
        return '{{for ({}) [{}]}}'.format(
            self.exp,
            self.context
        )
