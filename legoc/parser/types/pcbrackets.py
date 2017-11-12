from legoc.parser.types.pvalue import PValue
from legoc.parser.types.pexpression import PExpression
from legoc.parser.types.pboperation import PBOperation


class PCBrackets(PValue):
    def __init__(self):
        super(PCBrackets, self).__init__('')
        self.parents.add(PCBrackets.__name__)

        self.child = None

    def left_reduce(self, tkn):
        if 'PValue' in tkn.parents:
            oper = PBOperation('()')
            oper = oper.left_reduce(tkn)
            exp = oper.right_reduce(self)
            return exp

        return None

    def right_reduce(self, tkn):
        if 'PType' in tkn.parents:
            tkn.type = 'Function'
            tkn.prms = self.child
            return tkn

        return None

    def get(self):
        return self.child

    def __str__(self):
        if isinstance(self.child, list):
            return 'CB({})'.format(
                ', '.join([str(x) for x in self.child])
            )
        return 'CB({})'.format(
            self.child
        )
