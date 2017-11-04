from legoc.parser.types.pobject.pobject import PObject
from legoc.parser.types.pvalue.prvalue import PRValue
from legoc.parser.types.ptype.psimple_type import PSimpleType
from legoc.parser.types.ptype.ptemplate_type import PTemplateType


class PContainer(PObject):
    def __init__(self):
        super(PContainer, self).__init__()
        self.type_name = 'PContainer'
        self.complete = True

        self.type = PTemplateType('Container')
        self.lst = []

    @classmethod
    def b_b(cls, *_):
        self = cls()

        item_type = PSimpleType('Any')
        self.type.prm_types.append(item_type)

        return self

    @classmethod
    def b_o_b(cls, *_):
        self = cls()

        item_type = PSimpleType('Any')
        self.type.prm_types.append(item_type)

        return self

    @classmethod
    def b_item_b(cls, ob, val1, cb):
        self = cls()

        item_type = PSimpleType('Any')
        if isinstance(val1, PRValue):
            item_type = val1.type

        self.lst.append(val1)
        self.type.prm_types.append(item_type)

        return self

    @classmethod
    def b_itemlist_b(cls, obr, item_lst, cbr):
        self = cls()

        item_type = None
        for item in item_lst.lst:
            if isinstance(item, PRValue) and item_type is None:
                item_type = item.type

            elif isinstance(item, PRValue) and item_type != item.type:
                item_type = PSimpleType('Any')

            elif not isinstance(item, PRValue):
                item_type = PSimpleType('Any')

            self.lst.append(item)

        if item_type is None:
            item_type = PSimpleType('Any')

        self.type.prm_types.append(item_type)

        return self

    def __str__(self):
        return '{{{} {} [{}]}}'.format(
            self.type_name,
            self.type,
            ', '.join([str(x) for x in self.lst])
        )
