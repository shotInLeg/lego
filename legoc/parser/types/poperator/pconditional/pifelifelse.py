from legoc.parser.types.poperator.poperator import POperator


class PIfElifElse(POperator):
    def __init__(self, if_based):
        super(PIfElifElse, self).__init__(if_based.str_value)
        self.tstack.append(PIfElifElse.__name__)

    def get(self):
        return self
