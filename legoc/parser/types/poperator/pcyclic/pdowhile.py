from legoc.parser.types.poperator.poperator import POperator


class PDoWhile(POperator):
    def __init__(self, cond=None, context=None):
        super(PDoWhile, self).__init__('do')
        self.tstack.append(PDoWhile.__name__)

        self.cond = cond
        self.context = context

    def get(self):
        return self

    def __str__(self):
        return '{{do [{}] while ({})}}'.format(
            self.context, self.cond
        )
