from legoc.parser.types.poperator.poperator import POperator


class PWhile(POperator):
    def __init__(self, cond, context):
        super(PWhile, self).__init__('while')
        self.tstack.append(PWhile.__name__)

        self.cond = cond
        self.context = context

    def get(self):
        return self

    def __str__(self):
        return '{{while ({}) [{}]}}'.format(
            self.cond, self.context
        )
