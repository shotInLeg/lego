from legoc.parser.types.poperator.poperator import POperator


class PIfElifElse(POperator):
    def __init__(self, lexeme):
        super(PIfElifElse, self).__init__(lexeme)
        self.parents.add(PIfElifElse.__name__)

        self.cond = None
        self.then_cntx = None
        self.elif_cond = []
        self.elif_cntx = []
        self.else_cntx = None

    def right_reduce(self, tkn):
        if 'PFBrackets' in tkn.parents:
            self.else_cntx = tkn.get()
            self.complete = True
            return self

        return None

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

        view = '{} else {{{}}}'.format(
            view, self.else_cntx
        )

        return view
