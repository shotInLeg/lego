from legoc.parser.types.pobject.pobject import PObject
from legoc.parser.types.pvalue.prvalue import PRValue
from legoc.parser.types.ptype.psimple_type import PSimpleType
from legoc.parser.types.ptype.ptemplate_type import PTemplateType


class PVctrObject(PObject):
    def __init__(self):
        super(PVctrObject, self).__init__()
        self.type_name = 'PVctrObject'
        self.complete = True

        self.type = PTemplateType('Vctr')
        self.lst = []

    @staticmethod
    def bb(obr, cbr):
        vctr = PVctrObject()

        item_type = PSimpleType('Any')
        vctr.type.add_template_arg(item_type)

        return vctr

    @staticmethod
    def bvb(obr, val1, cbr):
        vctr = PVctrObject()

        item_type = PSimpleType('Any')
        if isinstance(val1, PRValue):
            item_type = val1.type

        vctr.lst.append(val1)

        vctr.type.add_template_arg(item_type)

        return vctr

    @staticmethod
    def belb(obr, expr_lst, cbr):
        vctr = PVctrObject()

        item_type = None
        for item in expr_lst.lst:
            if isinstance(item, PRValue) and item_type is None:
                item_type = item.type

            elif isinstance(item, PRValue) and item_type != item.type:
                item_type = PSimpleType('Any')

            elif not isinstance(item, PRValue):
                item_type = PSimpleType('Any')

            vctr.lst.append(item)

        if item_type is None:
            item_type = PSimpleType('Any')

        vctr.type.add_template_arg(item_type)

        return vctr

    def __str__(self):
        return '{{{} {} [{}]}}'.format(
            self.type_name,
            self.type,
            ', '.join([str(x) for x in self.lst])
        )
