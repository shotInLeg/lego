from legoc.parser.types.pvalue import PValue


class PSBrackets(PValue):
    def __init__(self):
        super(PSBrackets, self).__init__('')
        self.parents.add(PSBrackets.__name__)

        self.child = None

    def get(self):
        return self.child

    def __str__(self):
        if isinstance(self.child, list):
            return 'SB[{}]'.format(
                ', '.join([str(x) for x in self.child])
            )
        return 'SB[{}]'.format(
            self.child
        )
