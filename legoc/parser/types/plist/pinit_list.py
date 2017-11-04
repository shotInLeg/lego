from legoc.parser.types.plist.plist import PList


class PInitList(PList):
    def __init__(self):
        super(PInitList, self).__init__()
        self.type_name = 'PInitList'

    def __str__(self):
        return '{{LI {}}}'.format(
            ', '.join([str(x) for x in self.lst])
        )
