from legoc.parser.types.pvalue import PValue


class PConstant(PValue):
    def __init__(self, lexeme):
        super(PConstant, self).__init__(lexeme)
        self.parents.add(PConstant.__name__)

    def get(self):
        return self

    def __str__(self):
        return '{}'.format(
            self.str_value
        )
