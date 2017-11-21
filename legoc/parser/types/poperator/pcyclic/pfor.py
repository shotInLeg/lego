from legoc.parser.types.poperator.poperator import POperator


class PFor(POperator):
    def __init__(self, start=None, cond=None, step=None, context=None):
        super(PFor, self).__init__('for')
        self.tstack.append(PFor.__name__)

        self.start = start
        self.cond = cond
        self.step = step
        self.context = context

    def get(self):
        return self

    def __str__(self):
        return '{{for ({}; {}; {}) [{}]}}'.format(
            ','.join([str(x) for x in self.start]),
            self.cond,
            ','.join([str(x) for x in self.step]),
            self.context
        )
