from legoc.parser.types.ptype.pcomplex_type import PComplexType


class PFuncType(PComplexType):
    def __init__(self, lexem):
        super(PFuncType, self).__init__(lexem)
        self.type_name = 'PFuncType'

        self.prm_types = []

    @staticmethod
    def tbb(type1, ob, cb):
        ft = PFuncType(type1.str_value)

        return ft

    @staticmethod
    def tbtb(type1, ob, type2, cb):
        ft = PFuncType(type1.str_value)
        ft.prm_types.append(type2)

        return ft

    @staticmethod
    def tbtlb(type1, ob, type_list, cb):
        ft = PFuncType(type1.str_value)
        for typ in type_list.lst:
            ft.prm_types.append(typ)

        return ft

    def __str__(self):
        return '{{{} {}({})}}'.format(
            self.type_name,
            self.str_value,
            ','.join([str(x) for x in self.prm_types])
        )