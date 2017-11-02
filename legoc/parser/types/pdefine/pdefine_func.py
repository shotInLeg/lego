from legoc.parser.types.pdefine.pdefine import PDefine
from legoc.parser.types.ptype.pfunc_type import PFuncType
from legoc.parser.types.ptype.psimple_type import PSimpleType


class PDefineFunc(PDefine):
    def __init__(self):
        super(PDefineFunc, self).__init__()
        self.type_name = 'PDefineFunc'
        self.complete = True

        self.name = None
        self.form_params = []
        self.type = PFuncType('Any')
        self.value = None

    @staticmethod
    def nfov(name1, form, oper, val1):
        deffun = PDefineFunc()
        deffun.name = name1
        for prm in form.lst:
            deffun.form_params.append(prm)
            deffun.type.prm_types.append(PSimpleType('Any'))

        if val1.type_name == 'PExpression':
            deffun.value = val1.child
        else:
            deffun.value = val1

        return deffun

    @staticmethod
    def nfotv(name1, form, oper, type1, val1):
        if len(form.lst) != len(type1.prm_types):
            raise ValueError('Неверный тип функции')

        deffun = PDefineFunc()
        deffun.name = name1

        for prm in form.lst:
            deffun.form_params.append(prm)

        deffun.type = type1

        if val1.type_name == 'PExpression':
            deffun.value = val1.child
        else:
            deffun.value = val1

        return deffun

    def __str__(self):
        return '{{{} {} ({}) {} {}}}'.format(
            self.type_name,
            self.name,
            ', '.join([str(x) for x in self.form_params]),
            self.type,
            self.value
        )
