from legoc.parser.types.poperator.poperator import POperator
from legoc.parser.types.poperator.pif_elif_else import PIfElifElse


class PIfElif(POperator):
    right = ['elif', 'else']

    def __init__(self, lexeme):
        super(PIfElif, self).__init__(lexeme)
        self.parents.add(PIfElif.__name__)

        self.cond = None
        self.then_cntx = None
        self.elif_cond = []
        self.elif_cntx = []

    def right_reduce(self, tkn):

        if 'PValue' in tkn.parents:
            self.elif_cond.append(tkn.get())
            self.complete = False

        if 'PFBrackets' in tkn.parents:
            self.elif_cntx.append(tkn.get())
            self.complete = True

        if 'POperator' in tkn.parents and self.complete:
            if tkn.get().str_value in self.right:
                if tkn.get().str_value == 'elif':
                    return self

                elif tkn.get().str_value == 'else':
                    res = PIfElifElse(self.str_value)
                    res.cond = self.cond
                    res.then_cntx = self.then_cntx
                    res.elif_cond = self.elif_cond
                    res.elif_cntx = self.elif_cntx
                    return res

            else:
                raise ValueError('{}: Неожиданный оператор'.format(
                    tkn
                ))

        return self

    def get(self):
        return self

    def __str__(self):
        view = 'if {} {{{}}}'.format(
            self.cond,
            self.then_cntx
        )

        for cond, cntx in zip(self.elif_cond, self.elif_cntx):
            view = '{} elif {} {{{}}}'.format(
                view,
                cond,
                cntx
            )

        return view
