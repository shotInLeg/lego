from legoc.parser.types.poperator.poperator import POperator
from legoc.parser.types.poperator.pconditional.pelif import PElif
from legoc.parser.types.poperator.pconditional.pelse import PElse


class PIf(POperator):
    def __init__(self, cond, context):
        super(PIf, self).__init__('if')
        self.tstack.append(PIf.__name__)

        self.if_cond = cond
        self.if_contex = context
        self.elif_conds = []
        self.elif_contexts = []
        self.else_context = None

    def get(self):
        return self

    def add(self, tkn):
        if isinstance(tkn, PElif):
            return self.add_elif(tkn)

        elif isinstance(tkn, PElse):
            return self.add_else(tkn)

        else:
            raise ValueError('Ожидался elif или else: `{}`'.format(
                tkn
            ))

    def add_elif(self, tkn):
        if self.else_context is not None:
            raise ValueError('Условное выражение завершено `{}`'.format(
                tkn
            ))

        self.elif_conds.append(tkn.cond)
        self.elif_contexts.append(tkn.context)

        return self

    def add_else(self, tkn):
        self.else_context = tkn.context

        return self

    def __str__(self):
        lst_elif = []
        for cond, cntx in zip(self.elif_conds, self.elif_contexts):
            pelif = '{{elif ({}) [{}]'.format(cond, cntx)
            lst_elif.append(pelif)

        return '{{if ({}) [{}] \n{} \nelse [{}]}}'.format(
            self.if_cond, self.if_contex,
            '\n'.join(lst_elif),
            self.else_context
        )
