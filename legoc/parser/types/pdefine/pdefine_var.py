from legoc.parser.types.pdefine.pdefine import PDefine


class PDefineVar(PDefine):
    def __init__(self):
        super(PDefineVar, self).__init__()
        self.type_name = 'PDefineVar'
        self.complete = True

    @staticmethod
    def noc(name1, oper, const1):
        defvar = PDefine()
        defvar.name = name1
        defvar.type = const1.type
        defvar.value = const1

        return defvar

    @staticmethod
    def notr(name1, oper, type1, rval1):
        defvar = PDefine()
        defvar.name = name1
        defvar.type = type1
        if rval1.type_name == 'PExpression':
            defvar.value = rval1.child
        else:
            defvar.value = rval1

        return defvar
