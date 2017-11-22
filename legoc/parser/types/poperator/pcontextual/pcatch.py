from legoc.parser.types.poperator.poperator import POperator


class PCatch(POperator):
    def __init__(self, params=None, context=None):
        super(PCatch, self).__init__('catch')
        self.tstack.append(PCatch.__name__)

        self.params = params
        self.context = context

    def get(self):
        return self
