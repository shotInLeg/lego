from legoc.parser.types.pvalue.pvalue import PValue


class PRValue(PValue):
    def __init__(self):
        super(PRValue, self).__init__()
        self.tstack.append(PRValue.__name__)

    def get(self):
        return self
