from legoc.parser.types.pvalue import PValue


class PExpression(PValue):
    def __init__(self):
        super(PExpression, self).__init__('')
        self.parents.add(PExpression.__name__)

        self.child = None

    def get(self):
        return self.child

    def __str__(self):
        return 'Exp{{{}}}'.format(
            self.child
        )
