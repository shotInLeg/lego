from legoc.parser.types.poperator.poperator import POperator


class PIfElse(POperator):
    def __init__(self, lexeme):
        super(PIfElse, self).__init__(lexeme)
        self.parents.add(PIfElse.__name__)

        self.cond = None
        self.then_cntx = None
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
        return 'if {} {{{}}} else {{{}}}'.format(
            self.cond,
            self.then_cntx,
            self.else_cntx
        )
