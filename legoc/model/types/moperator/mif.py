from legoc.model.types.moperator.moperator import MOperator


class MIf(MOperator):
    def __init__(self, if_mexp, if_lst_instr,
                 lst_elif_mexp, lst_elif_lst_instr,
                 else_lst_instr):
        super(MIf, self).__init__()
        self.tstack.append(MIf.__name__)

        self.if_cond = if_mexp
        self.if_instructions = if_lst_instr

        self.lst_elif_cond = lst_elif_mexp
        self.lst_elif_instructions = lst_elif_lst_instr

        self.else_instructions = else_lst_instr
