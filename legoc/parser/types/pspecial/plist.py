from legoc.parser.types.pvalue.prvalue import PRValue


class PList(PRValue):
    def __init__(self, child=None):
        super(PList, self).__init__()
        self.tstack.append(PList.__name__)

        self.child = [] if child is None else child

    def get(self):
        return self

    def __str__(self):
        return '{{Lst[{}]}}'.format(
            ', '.join([str(x) for x in self.child])
        )
