from legoc.parser.types.plist.plist import PList


class PInstructionList(PList):
    def __init__(self):
        super(PInstructionList, self).__init__()
        self.type_name = 'PInstructionList'

    @classmethod
    def item_item(cls, item1, item2):
        self = cls()

        self.lst.append(item1.child)
        self.lst.append(item2.child)

        return self

    @classmethod
    def list_item(cls, lst, item):
        self = cls()

        for itm in lst.lst:
            self.lst.append(itm)
        self.lst.append(item.child)

        return self

    @classmethod
    def item_list(cls, item, lst):
        self = cls()

        self.lst.append(item.child)
        for itm in lst.lst:
            self.lst.append(itm)

        return self

    def __str__(self):
        return '{{LIN {}}}'.format(
            ', '.join([str(x) for x in self.lst])
        )
