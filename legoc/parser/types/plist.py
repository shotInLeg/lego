from legoc.parser.types.pvalue import PValue


class PList(PValue):
    def __init__(self):
        super(PList, self).__init__('')
        self.parents.add(PList.__name__)
        self.child = []

    def get(self):
        return self

    def __str__(self):
        return '{{L[{}]}}'.format(
            ', '.join([str(x) for x in self.child])
        )
