from legoc.parser.types.pexp.pexpression import PExpression
from legoc.parser.types.poperation.pbinoperation import PBinOperation


class PSBrackets(PExpression):
    def __init__(self, child=None):
        super(PSBrackets, self).__init__(child)
        self.tstack.append(PSBrackets.__name__)

    def get(self):
        return self

    def get_list(self):
        if isinstance(self.child, list):
            return self.child
        else:
            return [self.child]
