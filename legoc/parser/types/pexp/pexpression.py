from legoc.parser.types.pvalue.plvalue import PLValue


class PExpression(PLValue):
    def __init__(self, in_brackets=False):
        super(PExpression, self).__init__()
        self.tstack.append(PExpression.__name__)
        self.child = None
        self.brackets = in_brackets

    def get(self):
        return self.child
