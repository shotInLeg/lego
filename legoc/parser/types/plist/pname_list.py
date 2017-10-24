from legoc.parser.types.plist.pvalue_list import PValueList


class PNameList(PValueList):
    def __init__(self):
        super(PNameList, self).__init__()
        self.type_name = 'PNameList'

    @staticmethod
    def non(name1, oper, name2):
        self = PNameList()

        self.lst.append(name1)
        self.lst.append(name2)

        return self

    @staticmethod
    def lon(list1, oper, name2):
        list1.lst.append(name2)
        return list1

    def __str__(self):
        return '{{LN {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )
