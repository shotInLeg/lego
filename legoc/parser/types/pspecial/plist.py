from legoc.parser.types.pvalue.prvalue import PRValue
from legoc.parser.types.ptype.psimpletype import PSimpleType
from legoc.parser.types.ptype.ptempltype import PTemplType
from legoc.parser.types.poperation.pbinoperation import PBinOperation


class PList(PRValue):
    def __init__(self, child=None):
        super(PList, self).__init__()
        self.tstack.append(PList.__name__)

        self.type = PTemplType(
            PSimpleType('List'),
            [PSimpleType('Any')]
        )
        self.child = [] if child is None else child

    def get(self):
        return self

    def get_list(self):
        if isinstance(self.child, list):
            return self.child
        else:
            return [self.child]

    def left_reduce(self, tkn):
        if 'PType' in tkn.tstack:
            self.type = tkn
            return self

        elif 'PValue' in tkn.tstack:
            oper = PBinOperation('[]')
            oper = oper.left_reduce(tkn)
            exp = oper.right_reduce(self)
            return exp

        return None

    def __str__(self):
        return '{{{}[{}]}}'.format(
            self.type,
            ', '.join([str(x) for x in self.child])
        )
