from legoc.parser.types.pvalue import PValue


class PName(PValue):
    def __init__(self, lexeme):
        super(PName, self).__init__(lexeme)
        self.parents.add(PName.__name__)

    def get(self):
        return self

    def __str__(self):
        return '{}'.format(
            self.str_value
        )
