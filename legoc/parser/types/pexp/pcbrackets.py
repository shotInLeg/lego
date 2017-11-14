from legoc.parser.types.pexp.pexpression import PExpression
from legoc.parser.types.poperation.pbinoperation import PBinOperation


class PCBrackets(PExpression):
    def __init__(self, child=None):
        super(PCBrackets, self).__init__(child)
        self.tstack.append(PCBrackets.__name__)

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
        if 'PValue' in tkn.tstack:
            oper = PBinOperation('()')
            oper = oper.left_reduce(tkn)
            exp = oper.right_reduce(self)
            return exp

        return None
