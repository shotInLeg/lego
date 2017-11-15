from legoc.parser.types.pvalue.prvalue import PRValue


class PDict(PRValue):
    def __init__(self, child=None):
        super(PDict, self).__init__()
        self.tstack.append(PDict.__name__)

        self.child = [] if child is None else child

    def get(self):
        return self

    def __str__(self):
        return '{{Dct[{}]}}'.format(
            ', '.join([str(x) for x in self.child])
        )
