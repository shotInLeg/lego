from legoc.parser.types.ptype.ptype import PType


class PComplexType(PType):
    def __init__(self,lexem):
        super(PComplexType, self).__init__(lexem)
        self.type_name = 'PComplexType'

        self.prm_types = []

    @classmethod
    def type_b_b(cls, type1, ob, cb):
        self = cls(type1.str_value)
        return self

    @classmethod
    def type_b_type_b(cls, type1, ob, type2, cb):
        self = cls(type1.str_value)
        self.prm_types.append(type2)

        return self

    @classmethod
    def type_b_typelist_b(cls, type1, ob, type_list, cb):
        self = cls(type1.str_value)
        for typ in type_list.lst:
            self.prm_types.append(typ)

        return self

    def __str__(self):
        return '{{{} {}({})}}'.format(
            self.type_name,
            self.str_value,
            ','.join([str(x) for x in self.prm_types])
        )
