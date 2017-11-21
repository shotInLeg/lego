from legoc.parser.types.poperator.poperator import POperator


class PWith(POperator):
    def __init__(self, exp=None, context=None):
        super(PWith, self).__init__('with')
        self.tstack.append(PWith.__name__)

        self.exp = exp
        self.context = context

    def get(self):
        return self

    def __str__(self):
        return '{{with ({}) [{}]}}'.format(
            ','.join([str(x) for x in self.exp]),
            self.context
        )
