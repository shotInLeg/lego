from legoc.parser.types.plist.plist import PList


class PTypeList(PList):
    def __init__(self):
        super(PTypeList, self).__init__()
        self.type_name = 'PTypeList'

    @staticmethod
    def tot(type1, oper, type2):
        self = PTypeList()

        self.lst.append(type1)
        self.lst.append(type2)

        return self

    @staticmethod
    def lot(tlist1, oper, type2):
        tlist1.lst.append(type2)
        return tlist1

    def __str__(self):
        return '{{LT {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )
