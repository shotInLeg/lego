from legoc.parser.types.pvalue.prvalue import PRValue


class PStruct(PRValue):
    def __init__(self, child=None):
        super(PStruct, self).__init__()
        self.tstack.append(PStruct.__name__)

        self.child = [] if child is None else child

    def get(self):
        return self

    def __str__(self):
        return '{{Strc[{}]}}'.format(
            ', '.join([str(x) for x in self.child])
        )
