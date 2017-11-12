from legoc.parser.types.poperator.poperator import POperator
from legoc.parser.types.poperator.pif_elif import PIfElif
from legoc.parser.types.poperator.pif_else import PIfElse


class PIf(POperator):
    right = ['elif', 'else']

    def __init__(self, lexeme):
        super(PIf, self).__init__(lexeme)
        self.parents.add(PIf.__name__)

        self.cond = None
        self.then_cntx = None

    def get(self):
        return self

    def right_reduce(self, tkn):
        if 'PValue' in tkn.parents:
            self.cond = tkn.get()

        if 'PFBrackets' in tkn.parents:
            self.then_cntx = tkn.get()
            self.complete = True

        if 'POperator' in tkn.parents and self.complete:
            if tkn.get().str_value in self.right:
                if tkn.get().str_value == 'elif':
                    res = PIfElif(self.str_value)
                    res.cond = self.cond
                    res.then_cntx = self.then_cntx
                    return res

                elif tkn.get().str_value == 'else':
                    res = PIfElse(self.str_value)
                    res.cond = self.cond
                    res.then_cntx = self.then_cntx
                    return res
            else:
                raise ValueError('{}: Неожиданный оператор'.format(
                    tkn
                ))

        return self

    def __str__(self):
        return 'if {} {{{}}}'.format(
            self.cond,
            self.then_cntx
        )
