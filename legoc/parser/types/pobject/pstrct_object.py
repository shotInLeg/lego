from legoc.parser.types.pobject.pcontainer import PContainer
from legoc.parser.types.ptype.psimple_type import PSimpleType


class PStrctObject(PContainer):
    def __init__(self):
        super(PStrctObject, self).__init__()
        self.type_name = 'PStrctObject'
        self.complete = True

        self.type = PSimpleType('Strct')

    @classmethod
    def b_o_b(cls, *_):
        self = cls()
        return self

    @classmethod
    def b_item_b(cls, ob, val1, cb):
        self = cls()
        self.lst.append(val1)
        return self

    @classmethod
    def b_itemlist_b(cls, obr, item_lst, cbr):
        self = cls()

        for item in item_lst.lst:
            self.lst.append(item)

        return self
