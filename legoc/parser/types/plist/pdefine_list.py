from legoc.parser.types.plist.plist import PList


class PDefineList(PList):
    def __init__(self):
        super(PDefineList, self).__init__()
        self.type_name = 'PDefineList'

    @staticmethod
    def dod(def1, oper, def2):
        self = PDefineList()
        self.lst.append(def1)
        self.lst.append(def2)

        return self

    @staticmethod
    def dlod(def_list, oper, def2):
        def_list.lst.append(def2)
        return def_list

    def __str__(self):
        return '{{LD {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )