from legoc.parser.types.pexp.pexpression import PExpression
from legoc.parser.types.poperation.pbinoperation import PBinOperation
from legoc.parser.types.ptype.ptempltype import PTemplType


class PTBrackets(PExpression):
    def __init__(self, child=None):
        super(PTBrackets, self).__init__(child)
        self.tstack.append(PTBrackets.__name__)

    def get(self):
        if not isinstance(self.child, list):
            return self.child
        raise ValueError('Множественный дочерний элеемент\n'
                         'Возможно нужен get_list')

    def get_list(self):
        if isinstance(self.child, list):
            return self.child
        else:
            return [self.child]

    def left_reduce(self, tkn):
        if 'PSimpleType' in tkn.tstack:
            pttype = PTemplType(tkn)
            pttype.args = self.child if isinstance(self.child, list) \
                else [self.child]
            return pttype

        return None
