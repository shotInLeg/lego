from legoc.parser.types.plist.plist import PList


class PAssociativePairList(PList):
    def __init__(self):
        super(PAssociativePairList, self).__init__()
        self.type_name = 'PAssociativePairList'

    @staticmethod
    def apoap(apair1, oper, apair2):
        self = PAssociativePairList()
        self.lst.append(apair1)
        self.lst.append(apair2)

        return self

    @staticmethod
    def plod(aplist_list, oper, pair2):
        aplist_list.lst.append(pair2)
        return aplist_list

    def __str__(self):
        return '{{LAP {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )
