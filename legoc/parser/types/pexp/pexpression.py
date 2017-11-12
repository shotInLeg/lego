from legoc.parser.types.pvalue.plvalue import PLValue


class PExpression(PLValue):
    def __init__(self, child=None):
        super(PExpression, self).__init__()
        self.tstack.append(PExpression.__name__)
        self.child = child

    def get(self):
        return self.child
