from legoc.parser.types.pvalue.prvalue import PRValue
from legoc.parser.types.ptype.psimpletype import PSimpleType
from legoc.parser.types.ptype.ptempltype import PTemplType


class PDict(PRValue):
    def __init__(self, child=None):
        super(PDict, self).__init__()
        self.tstack.append(PDict.__name__)

        self.type = PTemplType(
            PSimpleType('Dct'),
            [PSimpleType('Any'), PSimpleType('Any')]
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

        return None


    def __str__(self):
        return '{{{}[{}]}}'.format(
            self.type,
            ', '.join([str(x) for x in self.child])
        )
