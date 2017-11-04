from legoc.parser.types.psequence.psequence import PSequence


class PContext(PSequence):
    def __init__(self):
        super(PContext, self).__init__()
        self.type_name = 'PContext'

    def __str__(self):
        return '{{CNT {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )
