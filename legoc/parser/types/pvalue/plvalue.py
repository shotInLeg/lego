from legoc.parser.types.pvalue.pvalue import PValue


class PLValue(PValue):
    def __init__(self):
        super(PLValue, self).__init__()
        self.tstack.append(PLValue.__name__)

    def get(self):
        return self
