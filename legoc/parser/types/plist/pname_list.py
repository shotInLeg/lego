from legoc.parser.types.plist.pvalue_list import PValueList


class PNameList(PValueList):
    def __init__(self):
        super(PNameList, self).__init__()
        self.type_name = 'PNameList'

    def __str__(self):
        return '{{LN {}}}'.format(
            ', '.join([str(x) for x in self.lst])
        )
