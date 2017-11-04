from legoc.parser.types.pinit.pinit import PInit
from legoc.parser.types.ptype.pfunc_type import PFuncType
from legoc.parser.types.ptype.psimple_type import PSimpleType
from legoc.parser.types.poperator.preturn_operator import PReturnOperator


class PInitFunc(PInit):
    def __init__(self):
        super(PInitFunc, self).__init__()
        self.type_name = 'PInitFunc'
        self.complete = True

        self.params = []
        self.type = PFuncType('Any')

    @classmethod
    def caller_o_context(cls, caller, _, context):
        if caller.obj.type_name != 'PName':
            raise ValueError('Неверное выражение инициализации функции')

        for prm in caller.params:
            if prm.type_name != 'PName':
                raise ValueError('Неверное выражение инициализации функции')

        self = cls()

        self.lvalue = caller.obj
        for prm in caller.params.lst:
            self.params.append(prm)
            self.type.prm_types.append(PSimpleType('Any'))

        if len(context.lst) == 1 and not isinstance(context.lst[0], PReturnOperator):
            context.lst[0] = PReturnOperator.o_item(None, context.lst[0])
        self.value = context

        return self

    @classmethod
    def caller_o_type_context(cls, caller, _, type1, context):
        if caller.obj.type_name != 'PName':
            raise ValueError('Неверное выражение инициализации функции')

        for prm in caller.params:
            if prm.type_name != 'PName':
                raise ValueError('Неверное выражение инициализации функции')

        if len(caller.params) != len(type1.prm_types):
            raise ValueError('Неверный тип функции')

        self = cls()

        self.lvalue = caller.obj
        for prm in caller.params:
            self.params.append(prm)
        self.type = type1

        if len(context.lst) == 1 and not isinstance(context.lst[0], PReturnOperator):
            context.lst[0] = PReturnOperator.o_item(None, context.lst[0])
        self.value = context

        return self

    @classmethod
    def lvalue_params_o_context(cls, lvalue, params, _, context):
        self = cls()

        self.lvalue = lvalue
        for prm in params.lst:
            self.params.append(prm)
            self.type.prm_types.append(PSimpleType('Any'))

        if len(context.lst) == 1 and not isinstance(context.lst[0], PReturnOperator):
            context.lst[0] = PReturnOperator.o_item(None, context.lst[0])
        self.value = context

        return self

    @classmethod
    def lvalue_params_o_type_context(cls, lvalue, params, _, type1, context):
        if len(params.lst) != len(type1.prm_types):
            raise ValueError('Неверный тип функции')

        self = cls()

        self.lvalue = lvalue

        for prm in params.lst:
            self.params.append(prm)
        self.type = type1

        if len(context.lst) == 1 and not isinstance(context.lst[0], PReturnOperator):
            context.lst[0] = PReturnOperator.o_item(None, context.lst[0])
        self.value = context

        return self

    def __str__(self):
        return '{{{} {} ({}) {} {}}}'.format(
            self.type_name,
            self.lvalue,
            ', '.join([str(x) for x in self.params]),
            self.type,
            self.value
        )
