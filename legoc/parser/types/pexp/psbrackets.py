from legoc.parser.types.pexp.pexpression import PExpression


class PSBrackets(PExpression):
    def __init__(self, child=None):
        super(PSBrackets, self).__init__(child)
        self.tstack.append(PSBrackets.__name__)

    def get(self):
        if not isinstance(self.child, list):
            return self.child
        raise ValueError('Множественный дочерний элеемент\n'
                         'Возможно нужен get_list')

    def get_list(self):
        if not isinstance(self.child, list):
            return self.child
        else:
            return [self.child]
