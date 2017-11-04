from legoc.parser.types.pobject.pcontainer import PContainer
from legoc.parser.types.ptype.psimple_type import PSimpleType
from legoc.parser.types.ptype.ptemplate_type import PTemplateType
from legoc.parser.types.pvalue.prvalue import PRValue


class PDictObject(PContainer):
    def __init__(self):
        super(PDictObject, self).__init__()
        self.type_name = 'PDictObject'
        self.complete = True

        self.type = PTemplateType('Dct')

    @classmethod
    def b_o_b(cls, *_):
        self = cls()

        key_type = PSimpleType('Any')
        value_type = PSimpleType('Any')
        self.type.prm_types.append(key_type)
        self.type.prm_types.append(value_type)

        return self

    @classmethod
    def b_item_b(cls, ob, item, cb):
        self = cls()

        key_type = item.key_type
        value_type = item.value_type
        self.lst.append(item)
        self.type.prm_types.append(key_type)
        self.type.prm_types.append(value_type)

        return self

    @classmethod
    def b_itemlist_b(cls, obr, item_lst, cbr):
        self = cls()

        key_type = None
        value_type = None
        for item in item_lst.lst:
            if key_type is None:
                key_type = item.key_type

            elif key_type != item.key_type:
                key_type = PSimpleType('Any')

            if value_type is None:
                value_type = item.value_type

            elif value_type != item.value_type:
                value_type = PSimpleType('Any')

            self.lst.append(item)

        self.type.prm_types.append(key_type)
        self.type.prm_types.append(value_type)

        return self
