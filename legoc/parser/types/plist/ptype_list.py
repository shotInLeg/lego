from legoc.parser.types.plist.plist import PList


class PTypeList(PList):
    def __init__(self):
        super(PTypeList, self).__init__()
        self.type_name = 'PTypeList'

    def __str__(self):
        return '{{LT {}}}'.format(
            ', '.join([str(x) for x in self.lst])
        )
