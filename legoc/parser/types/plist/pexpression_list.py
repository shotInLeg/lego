from legoc.parser.types.plist.pvalue_list import PValueList


class PExpressionList(PValueList):
    def __init__(self):
        super(PExpressionList, self).__init__()
        self.type_name = 'PExpressionList'

    def __str__(self):
        return '{{LE {}}}'.format(
            ', '.join([str(x) for x in self.lst])
        )
