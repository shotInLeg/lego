from legoc.parser.types.pobject.pobject import PObject
from legoc.parser.types.ptype.psimple_type import PSimpleType
from legoc.parser.types.ptype.ptemplate_type import PTemplateType


class PDictObject(PObject):
    def __init__(self):
        super(PDictObject, self).__init__()
        self.type_name = 'PDictObject'
        self.complete = True

        self.type = PTemplateType('Dct')
        self.lst = []

    @staticmethod
    def bob(obr, opr, cbr):
        vctr = PDictObject()

        key_type = PSimpleType('Any')
        value_type = PSimpleType('Any')
        vctr.type.add_template_arg(key_type)
        vctr.type.add_template_arg(value_type)

        return vctr

    @staticmethod
    def bpb(obr, ap1, cbr):
        vctr = PDictObject()

        key_type = ap1.key_type
        value_type = ap1.value_type
        vctr.type.add_template_arg(key_type)
        vctr.type.add_template_arg(value_type)

        vctr.lst.append(ap1)

        return vctr

    @staticmethod
    def bplb(obr, apl_lst, cbr):
        vctr = PDictObject()

        key_type = None
        value_type = None
        for item in apl_lst.lst:
            if key_type is None and value_type is None:
                key_type = item.key_type
                value_type = item.value_type

            if key_type != item.key_type:
                key_type = PSimpleType('Any')

            if value_type != item.value_type:
                value_type = PSimpleType('Any')

            vctr.lst.append(item)

        if key_type is None:
            key_type = PSimpleType('Any')
        if value_type is None:
            value_type = PSimpleType('Any')

        vctr.type.add_template_arg(key_type)
        vctr.type.add_template_arg(value_type)

        return vctr

    def __str__(self):
        return '{{{} {} [{}]}}'.format(
            self.type_name,
            self.type,
            ', '.join([str(x) for x in self.lst])
        )
