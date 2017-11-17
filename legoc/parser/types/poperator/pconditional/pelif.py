from legoc.parser.types.poperator.poperator import POperator


class PElif(POperator):
    def __init__(self, cond, context):
        super(PElif, self).__init__('elif')
        self.tstack.append(PElif.__name__)

        self.cond = cond
        self.context = context

    def get(self):
        return self
