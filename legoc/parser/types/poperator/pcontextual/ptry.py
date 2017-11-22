from legoc.parser.types.poperator.poperator import POperator
from legoc.parser.types.poperator.pcontextual.pcatch import PCatch
from legoc.parser.types.poperator.pcontextual.pfinally import PFinally


class PTry(POperator):
    def __init__(self, context=None):
        super(PTry, self).__init__('with')
        self.tstack.append(PTry.__name__)

        self.context = context
        self.catch_params = []
        self.catch_context = []
        self.finally_context = None

    def get(self):
        return self

    def add(self, tkn):
        if isinstance(tkn, PCatch):
            return self.add_catch(tkn)

        elif isinstance(tkn, PFinally):
            return self.add_finally(tkn)

        else:
            raise ValueError('Ожидался catch или finally: `{}`'.format(
                tkn
            ))

    def add_catch(self, tkn):
        if self.finally_context is not None:
            raise ValueError('try выражение завершено `{}`'.format(
                tkn
            ))

        self.catch_params.append(tkn.params)
        self.catch_context.append(tkn.context)

        return self

    def add_finally(self, tkn):
        self.finally_context = tkn.context

        return self

    def __str__(self):
        lst_elif = []
        for cond, cntx in zip(self.catch_params, self.catch_context):
            pcatch = '{{catch ({}) [{}]'.format(cond, cntx)
            lst_elif.append(pcatch)

        return '{{try [{}] \n{} \nfinally [{}]}}'.format(
            self.context,
            '\n'.join(lst_elif),
            self.finally_context
        )
