from legoc.parser.types.poperator.poperator import POperator


class PElse(POperator):
    def __init__(self, context):
        super(PElse, self).__init__('else')
        self.tstack.append(PElse.__name__)

        self.context = context

    def get(self):
        return self
