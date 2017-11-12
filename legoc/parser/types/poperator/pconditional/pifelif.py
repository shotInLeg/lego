from legoc.parser.types.poperator.poperator import POperator


class PIfElif(POperator):
    def __init__(self, if_based):
        super(PIfElif, self).__init__(if_based.str_value)
        self.tstack.append(PIfElif.__name__)

    def get(self):
        return self
