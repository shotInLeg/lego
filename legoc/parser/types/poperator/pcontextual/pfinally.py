from legoc.parser.types.poperator.poperator import POperator


class PFinally(POperator):
    def __init__(self, context=None):
        super(PFinally, self).__init__('finally')
        self.tstack.append(PFinally.__name__)

        self.context = context

    def get(self):
        return self
