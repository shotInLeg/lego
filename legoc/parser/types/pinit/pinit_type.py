from legoc.parser.types.pinit.pinit import PInit
from legoc.parser.types.ptype.pfunc_type import PFuncType
from legoc.parser.types.ptype.psimple_type import PSimpleType


class PInitType(PInit):
    def __init__(self):
        super(PInitType, self).__init__()
        self.type_name = 'PInitType'
        self.complete = True

        self.parents = []
        self.type = PSimpleType('Type')
        self.value = None

    @classmethod
    def lvalue_o_value(cls, lvalue, _, value):
        self = cls()

        self.lvalue = lvalue
        self.value = value

        return self

    @classmethod
    def lvalue_o_type_value(cls, lvalue, _, type1, value):
        self = cls()

        self.lvalue = lvalue

        for parent in type1.prm_types:
            self.parents.append(parent)

        self.value = value

        return self

    def __str__(self):
        return '{{{} {} {}({}) {}}}'.format(
            self.type_name,
            self.lvalue,
            self.type,
            ', '.join([str(x) for x in self.parents]),
            self.value
        )
