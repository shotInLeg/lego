from legoc.parser.types.plist.plist import PList


class PAssociativePairList(PList):
    def __init__(self):
        super(PAssociativePairList, self).__init__()
        self.type_name = 'PAssociativePairList'

    def __str__(self):
        return '{{LAP {}}}'.format(
            ', '.join([str(x) for x in self.lst])
        )
