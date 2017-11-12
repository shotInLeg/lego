from legoc.parser.types.poperator.poperator import POperator


class PIfElse(POperator):
    def __init__(self, if_based):
        super(PIfElse, self).__init__(if_based.str_value)
        self.tstack.append(PIfElse.__name__)

    def get(self):
        return self
